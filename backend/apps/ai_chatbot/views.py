"""
AI Chatbot views
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import ChatbotConfiguration, ChatbotKnowledgeBase, ChatConversation, ChatbotIntent
from .serializers import (
    ChatbotConfigurationSerializer, ChatbotConfigurationCreateSerializer,
    ChatbotKnowledgeBaseSerializer, ChatConversationSerializer,
    ChatbotIntentSerializer, ChatMessageSerializer
)
from .chatbot_service import ChatbotService
import uuid


class ChatbotConfigurationViewSet(viewsets.ModelViewSet):
    """Chatbot configuration CRUD"""
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ChatbotConfigurationCreateSerializer
        return ChatbotConfigurationSerializer
    
    def get_queryset(self):
        return ChatbotConfiguration.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def test_connection(self, request, pk=None):
        """Test chatbot AI provider connection"""
        config = self.get_object()
        
        try:
            service = ChatbotService(config)
            test_response = service.get_response(
                message="Hello, this is a test message.",
                session_id=f"test_{uuid.uuid4()}"
            )
            
            return Response({
                'success': test_response['success'],
                'message': 'Connection successful!' if test_response['success'] else 'Connection failed',
                'test_response': test_response.get('response', '')
            })
        except Exception as e:
            return Response({
                'success': False,
                'message': f'Connection failed: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)


class ChatbotKnowledgeBaseViewSet(viewsets.ModelViewSet):
    """Knowledge base CRUD"""
    serializer_class = ChatbotKnowledgeBaseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            config = ChatbotConfiguration.objects.get(user=self.request.user)
            return ChatbotKnowledgeBase.objects.filter(chatbot=config)
        except ChatbotConfiguration.DoesNotExist:
            return ChatbotKnowledgeBase.objects.none()
    
    def perform_create(self, serializer):
        config = ChatbotConfiguration.objects.get(user=self.request.user)
        serializer.save(chatbot=config)


class ChatConversationViewSet(viewsets.ReadOnlyModelViewSet):
    """View conversations"""
    serializer_class = ChatConversationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            config = ChatbotConfiguration.objects.get(user=self.request.user)
            return ChatConversation.objects.filter(chatbot=config)
        except ChatbotConfiguration.DoesNotExist:
            return ChatConversation.objects.none()


class ChatbotIntentViewSet(viewsets.ModelViewSet):
    """Custom intents CRUD"""
    serializer_class = ChatbotIntentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        try:
            config = ChatbotConfiguration.objects.get(user=self.request.user)
            return ChatbotIntent.objects.filter(chatbot=config)
        except ChatbotConfiguration.DoesNotExist:
            return ChatbotIntent.objects.none()
    
    def perform_create(self, serializer):
        config = ChatbotConfiguration.objects.get(user=self.request.user)
        serializer.save(chatbot=config)


@api_view(['POST'])
@permission_classes([AllowAny])
def chat_message(request):
    """Send a chat message and get response"""
    serializer = ChatMessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    message = serializer.validated_data['message']
    session_id = serializer.validated_data['session_id']
    context = serializer.validated_data.get('context', {})
    
    # Get user's chatbot config
    # For now, we'll use a default admin chatbot if user not authenticated
    try:
        if request.user.is_authenticated:
            service = ChatbotService(request.user)
        else:
            # Use the first active chatbot (admin's)
            from django.contrib.auth import get_user_model
            User = get_user_model()
            admin_user = User.objects.filter(role='admin', is_active=True).first()
            if not admin_user:
                return Response({
                    'success': False,
                    'error': 'No chatbot configured'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            service = ChatbotService(admin_user)
        
        result = service.get_response(message, session_id, context)
        
        return Response(result)
    
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
