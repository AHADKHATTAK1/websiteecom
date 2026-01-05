"""
AI Chatbot Service - Multi-provider support
"""
import openai
import anthropic
import google.generativeai as genai
from django.utils import timezone
from .models import ChatbotConfiguration, ChatConversation, ChatbotKnowledgeBase
from apps.products.models import Product
from apps.orders.models import Order


class ChatbotService:
    """Main chatbot service handling all AI providers"""
    
    def __init__(self, user_or_config):
        if isinstance(user_or_config, ChatbotConfiguration):
            self.config = user_or_config
        else:
            self.config = ChatbotConfiguration.objects.get(user=user_or_config)
        
        self.setup_provider()
    
    def setup_provider(self):
        """Initialize AI provider based on configuration"""
        api_key = self.config.get_api_key()
        
        if self.config.ai_provider == 'openai':
            openai.api_key = api_key
        elif self.config.ai_provider == 'claude':
            self.anthropic_client = anthropic.Anthropic(api_key=api_key)
        elif self.config.ai_provider == 'gemini':
            genai.configure(api_key=api_key)
            self.gemini_model = genai.GenerativeModel(self.config.model_name)
    
    def get_response(self, message, session_id, context=None):
        """Get AI response based on provider"""
        try:
            # Load conversation history
            conversation = self.get_conversation(session_id)
            
            # Build enhanced prompt with context
            enhanced_message = self.build_context_message(message, context)
            
            # Get response from appropriate provider
            if self.config.ai_provider == 'openai':
                response_text = self.openai_response(enhanced_message, conversation)
            elif self.config.ai_provider == 'claude':
                response_text = self.claude_response(enhanced_message, conversation)
            elif self.config.ai_provider == 'gemini':
                response_text = self.gemini_response(enhanced_message, conversation)
            else:
                response_text = self.config.fallback_message
            
            # Save conversation
            self.save_conversation(session_id, message, response_text)
            
            return {
                'success': True,
                'response': response_text,
                'session_id': session_id
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'response': self.config.fallback_message
            }
    
    def openai_response(self, message, conversation_history):
        """Get response from OpenAI"""
        messages = [{"role": "system", "content": self.config.system_prompt}]
        
        # Add conversation history
        for msg in conversation_history[-10:]:  # Last 10 messages
            messages.append({
                "role": msg['role'],
                "content": msg['content']
            })
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        response = openai.ChatCompletion.create(
            model=self.config.model_name,
            messages=messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens
        )
        
        return response.choices[0].message.content
    
    def claude_response(self, message, conversation_history):
        """Get response from Claude"""
        messages = []
        
        # Format conversation history for Claude
        for msg in conversation_history[-10:]:
            messages.append({
                "role": msg['role'],
                "content": msg['content']
            })
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        response = self.anthropic_client.messages.create(
            model=self.config.model_name,
            max_tokens=self.config.max_tokens,
            system=self.config.system_prompt,
            messages=messages
        )
        
        return response.content[0].text
    
    def gemini_response(self, message, conversation_history):
        """Get response from Gemini"""
        # Build conversation for Gemini
        chat = self.gemini_model.start_chat(history=[])
        
        # Add system prompt as first message
        full_message = f"{self.config.system_prompt}\n\nUser: {message}"
        
        response = chat.send_message(full_message)
        return response.text
    
    def build_context_message(self, message, context=None):
        """Build message with additional context"""
        if not context:
            return message
        
        context_parts = [message]
        
        # Add product context
        if self.config.enable_product_recommendations and 'product_query' in context:
            products = self.get_relevant_products(context['product_query'])
            if products:
                product_info = "\n".join([
                    f"- {p.name}: ${p.price}" for p in products[:5]
                ])
                context_parts.append(f"\nAvailable products:\n{product_info}")
        
        # Add knowledge base
        if self.config.enable_knowledge_base:
            kb_items = self.search_knowledge_base(message)
            if kb_items:
                kb_info = "\n".join([kb.content for kb in kb_items[:2]])
                context_parts.append(f"\nKnowledge base:\n{kb_info}")
        
        return "\n".join(context_parts)
    
    def get_conversation(self, session_id):
        """Get conversation history"""
        try:
            conversation = ChatConversation.objects.get(
                chatbot=self.config,
                session_id=session_id
            )
            return conversation.messages
        except ChatConversation.DoesNotExist:
            return []
    
    def save_conversation(self, session_id, user_message, ai_response):
        """Save conversation to database"""
        conversation, created = ChatConversation.objects.get_or_create(
            chatbot=self.config,
            session_id=session_id
        )
        
        timestamp = timezone.now().isoformat()
        
        conversation.messages.append({
            "role": "user",
            "content": user_message,
            "timestamp": timestamp
        })
        
        conversation.messages.append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": timestamp
        })
        
        conversation.save()
    
    def get_relevant_products(self, query):
        """Search for relevant products (tenant-aware)"""
        try:
            from apps.products.models import Product
            # Get store from chatbot configuration
            store = getattr(self.config, 'store', None)
            
            products = Product.objects.filter(name__icontains=query)
            
            # Filter by store if multi-tenant
            if store:
                products = products.filter(store=store)
            
            return products[:5]
        except:
            return []
    
    def search_knowledge_base(self, query):
        """Search knowledge base"""
        return ChatbotKnowledgeBase.objects.filter(
            chatbot=self.config,
            is_active=True,
            content__icontains=query
        )[:2]
