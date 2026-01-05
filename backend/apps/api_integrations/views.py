"""
API Integrations views
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import APIProvider, APIConfiguration, APILog
from .serializers import (
    APIProviderSerializer, APIConfigurationSerializer,
    APIConfigurationCreateSerializer, APILogSerializer
)
from .providers.payment.stripe_integration import StripeIntegration
from .providers.email.sendgrid_integration import SendGridIntegration
from .providers.sms.twilio_integration import TwilioIntegration


class APIProviderViewSet(viewsets.ReadOnlyModelViewSet):
    """List available API providers"""
    queryset = APIProvider.objects.filter(is_active=True)
    serializer_class = APIProviderSerializer
    permission_classes = [IsAuthenticated]


class APIConfigurationViewSet(viewsets.ModelViewSet):
    """Manage API configurations"""
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return APIConfigurationCreateSerializer
        return APIConfigurationSerializer
    
    def get_queryset(self):
        return APIConfiguration.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def test_connection(self, request, pk=None):
        """Test API connection"""
        config = self.get_object()
        
        try:
            # Get the appropriate integration
            provider_slug = config.provider.slug
            
            if provider_slug == 'stripe':
                integration = StripeIntegration(config)
            elif provider_slug == 'sendgrid':
                integration = SendGridIntegration(config)
            elif provider_slug == 'twilio':
                integration = TwilioIntegration(config)
            else:
                return Response({
                    'success': False,
                    'message': 'Integration not implemented yet'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            result = integration.test_connection()
            
            # Update configuration
            config.last_tested_at = timezone.now()
            config.test_status = 'success' if result['success'] else 'failed'
            config.test_message = result.get('message', '')
            config.save()
            
            return Response(result)
        
        except Exception as e:
            config.last_tested_at = timezone.now()
            config.test_status = 'failed'
            config.test_message = str(e)
            config.save()
            
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def logs(self, request, pk=None):
        """Get API logs"""
        config = self.get_object()
        logs = APILog.objects.filter(configuration=config).order_by('-created_at')[:100]
        serializer = APILogSerializer(logs, many=True)
        return Response(serializer.data)
