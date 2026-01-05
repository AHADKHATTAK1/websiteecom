"""
AI Chatbot URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'config', views.ChatbotConfigurationViewSet, basename='chatbot-config')
router.register(r'knowledge-base', views.ChatbotKnowledgeBaseViewSet, basename='knowledge-base')
router.register(r'conversations', views.ChatConversationViewSet, basename='conversations')
router.register(r'intents', views.ChatbotIntentViewSet, basename='intents')

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', views.chat_message, name='chat-message'),
]
