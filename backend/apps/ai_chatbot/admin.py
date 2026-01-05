"""
Admin configuration for AI chatbot
"""
from django.contrib import admin
from .models import ChatbotConfiguration, ChatbotKnowledgeBase, ChatConversation, ChatbotIntent


@admin.register(ChatbotConfiguration)
class ChatbotConfigurationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'ai_provider', 'model_name', 'is_active', 'created_at']
    list_filter = ['ai_provider', 'is_active']
    search_fields = ['user__email', 'name', 'model_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Info', {'fields': ('user', 'name', 'is_active')}),
        ('AI Provider', {'fields': ('ai_provider', 'model_name', 'api_key', 'api_endpoint')}),
        ('Model Parameters', {'fields': ('system_prompt', 'temperature', 'max_tokens')}),
        ('Messages', {'fields': ('greeting_message', 'fallback_message', 'offline_message')}),
        ('Appearance', {'fields': ('appearance',)}),
        ('Features', {'fields': ('enable_knowledge_base', 'enable_product_recommendations', 'enable_order_tracking')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(ChatbotKnowledgeBase)
class ChatbotKnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'chatbot', 'category', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']
    search_fields = ['title', 'content', 'category']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ChatConversation)
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'chatbot', 'customer_email', 'sentiment', 'is_resolved', 'rating', 'created_at']
    list_filter = ['is_resolved', 'sentiment', 'rating', 'created_at']
    search_fields = ['session_id', 'customer_email', 'customer_name']
    readonly_fields = ['session_id', 'messages', 'created_at', 'updated_at']
    
    def has_add_permission(self, request):
        return False


@admin.register(ChatbotIntent)
class ChatbotIntentAdmin(admin.ModelAdmin):
    list_display = ['name', 'chatbot', 'priority', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
