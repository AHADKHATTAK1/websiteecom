"""
AI Chatbot Models
"""
from django.db import models
from django.contrib.auth import get_user_model
from core.base_models import TimeStampedModel
from utils.encryption import encryption_service

User = get_user_model()


class ChatbotConfiguration(TimeStampedModel):
    """Main chatbot configuration"""
    
    AI_PROVIDER_CHOICES = [
        ('openai', 'OpenAI'),
        ('claude', 'Anthropic Claude'),
        ('gemini', 'Google Gemini'),
        ('custom', 'Custom Model'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chatbot_config')
    
    # Basic settings
    name = models.CharField(max_length=100, default="AI Assistant")
    is_active = models.BooleanField(default=True)
    
    # AI Provider settings
    ai_provider = models.CharField(max_length=50, choices=AI_PROVIDER_CHOICES)
    model_name = models.CharField(max_length=100)  # gpt-4, claude-3, gemini-pro
    api_key = models.TextField()  # Encrypted
    api_endpoint = models.URLField(blank=True)  # For custom models
    
    # Model parameters
    system_prompt = models.TextField(default="You are a helpful e-commerce assistant.")
    temperature = models.FloatField(default=0.7)
    max_tokens = models.IntegerField(default=500)
    
    # Messages
    greeting_message = models.TextField(default="Hello! How can I help you today?")
    fallback_message = models.TextField(default="I'm sorry, I didn't understand that. Can you rephrase?")
    offline_message = models.TextField(default="Our chatbot is currently offline. Please try again later.")
    
    # Appearance settings
    appearance = models.JSONField(default=dict)  # {position, colors, avatar}
    
    # Features
    enable_knowledge_base = models.BooleanField(default=True)
    enable_product_recommendations = models.BooleanField(default=True)
    enable_order_tracking = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'chatbot_configurations'
    
    def __str__(self):
        return f"{self.user.email} - {self.name}"
    
    def set_api_key(self, raw_key):
        """Encrypt and set API key"""
        self.api_key = encryption_service.encrypt(raw_key)
    
    def get_api_key(self):
        """Decrypt and get API key"""
        return encryption_service.decrypt(self.api_key)


class ChatbotKnowledgeBase(TimeStampedModel):
    """Custom training data for chatbot"""
    
    chatbot = models.ForeignKey(ChatbotConfiguration, on_delete=models.CASCADE, related_name='knowledge_base')
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(default=list)
    
    # For vector search (optional)
    embeddings = models.JSONField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'chatbot_knowledge_base'
    
    def __str__(self):
        return self.title


class ChatConversation(TimeStampedModel):
    """Store chat conversations"""
    
    chatbot = models.ForeignKey(ChatbotConfiguration, on_delete=models.CASCADE, related_name='conversations')
    
    session_id = models.CharField(max_length=100, db_index=True)
    customer_email = models.EmailField(blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    
    # Conversation data
    messages = models.JSONField(default=list)  # [{role, content, timestamp}]
    
    # Analytics
    sentiment = models.CharField(max_length=20, blank=True)  # positive, negative, neutral
    is_resolved = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=True)  # 1-5 stars
    
    # Metadata
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    class Meta:
        db_table = 'chat_conversations'
        indexes = [
            models.Index(fields=['session_id']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return f"Conversation {self.session_id}"


class ChatbotIntent(TimeStampedModel):
    """Define custom intents and responses"""
    
    chatbot = models.ForeignKey(ChatbotConfiguration, on_delete=models.CASCADE, related_name='intents')
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Training
    training_phrases = models.JSONField(default=list)  # List of example phrases
    response = models.TextField() # Response template
    
    # Action
    action = models.CharField(max_length=100, blank=True)  # e.g., 'track_order', 'recommend_products'
    action_parameters = models.JSONField(default=dict)
    
    priority = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'chatbot_intents'
        ordering = ['-priority', 'name']
    
    def __str__(self):
        return self.name
