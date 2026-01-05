"""
WebSocket Consumer for real-time chat
"""
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .chatbot_service import ChatbotService
from .models import ChatbotConfiguration


class ChatConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for chat"""
    
    async def connect(self):
        """Handle WebSocket connection"""
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.room_group_name = f'chat_{self.session_id}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'welcome',
            'message': 'Connected to chatbot'
        }))
    
    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        """Receive message from WebSocket"""
        try:
            data = json.loads(text_data)
            message= data.get('message', '')
            user_id = data.get('user_id')
            
            if not message:
                return
            
            # Get bot response
            response_data = await self.get_bot_response(user_id, message, self.session_id)
            
            # Send response
            await self.send(text_data=json.dumps(response_data))
        
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'error': str(e)
            }))
    
    @database_sync_to_async
    def get_bot_response(self, user_id, message, session_id):
        """Get response from chatbot service"""
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        try:
            # Get user's chatbot config
            user = User.objects.get(id=user_id)
            service = ChatbotService(user)
            
            result = service.get_response(message, session_id)
            
            return {
                'type': 'message',
                'message': result['response'],
                'success': result['success']
            }
        except Exception as e:
            return {
                'type': 'error',
                'error': str(e)
            }
