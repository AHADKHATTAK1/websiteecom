"""
AI Chatbot serializers
"""
from rest_framework import serializers
from .models import ChatbotConfiguration, ChatbotKnowledgeBase, ChatConversation, ChatbotIntent


class ChatbotConfigurationSerializer(serializers.ModelSerializer):
    """Chatbot configuration serializer"""
    api_key_encrypted = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatbotConfiguration
        fields = ['id', 'name', 'is_active', 'ai_provider', 'model_name',
                  'system_prompt', 'temperature', 'max_tokens',
                  'greeting_message', 'fallback_message', 'offline_message',
                  'appearance', 'enable_knowledge_base',
                  'enable_product_recommendations', 'enable_order_tracking',
                  'api_key_encrypted', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'api_key_encrypted']
    
    def get_api_key_encrypted(self, obj):
        """Show if API key is set"""
        return bool(obj.api_key)


class ChatbotConfigurationCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating chatbot config"""
    raw_api_key = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = ChatbotConfiguration
        fields = ['name', 'is_active', 'ai_provider', 'model_name',
                  'raw_api_key', 'api_endpoint', 'system_prompt',
                  'temperature', 'max_tokens', 'greeting_message',
                  'fallback_message', 'offline_message', 'appearance',
                  'enable_knowledge_base', 'enable_product_recommendations',
                  'enable_order_tracking']
    
    def create(self, validated_data):
        raw_api_key = validated_data.pop('raw_api_key', None)
        instance = super().create(validated_data)
        
        if raw_api_key:
            instance.set_api_key(raw_api_key)
            instance.save()
        
        return instance
    
    def update(self, instance, validated_data):
        raw_api_key = validated_data.pop('raw_api_key', None)
        instance = super().update(instance, validated_data)
        
        if raw_api_key:
            instance.set_api_key(raw_api_key)
            instance.save()
        
        return instance


class ChatbotKnowledgeBaseSerializer(serializers.ModelSerializer):
    """Knowledge base serializer"""
    
    class Meta:
        model = ChatbotKnowledgeBase
        fields = ['id', 'title', 'content', 'category', 'tags',
                  'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ChatConversationSerializer(serializers.ModelSerializer):
    """Conversation serializer"""
    
    class Meta:
        model = ChatConversation
        fields = ['id', 'session_id', 'customer_email', 'customer_name',
                  'messages', 'sentiment', 'is_resolved', 'rating',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ChatbotIntentSerializer(serializers.ModelSerializer):
    """Intent serializer"""
    
    class Meta:
        model = ChatbotIntent
        fields = ['id', 'name', 'description', 'training_phrases',
                  'response', 'action', 'action_parameters',
                  'priority', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ChatMessageSerializer(serializers.Serializer):
    """Serializer for chat messages"""
    message = serializers.CharField()
    session_id = serializers.CharField()
    context = serializers.JSONField(required=False)
