"""
Twilio SMS Integration
"""
from twilio.rest import Client
from apps.api_integrations.api_manager import BaseAPIManager



class TwilioIntegration(BaseAPIManager):
    """Twilio SMS service integration"""
    
    def __init__(self, configuration):
        super().__init__(configuration)
        # Twilio uses account_sid as api_key and auth_token as api_secret
        self.client = Client(self.api_key, self.api_secret)
        self.from_number = self.extra_config.get('from_number', '')
    
    def _get_auth_headers(self):
        return {}
    
    def test_connection(self):
        """Test Twilio connection"""
        try:
            account = self.client.api.accounts(self.api_key).fetch()
            return {
                'success': True,
                'message': f'Connected to Twilio account: {account.friendly_name}',
                'account_id': account.sid
            }
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
    
    def send_sms(self, to_number, message_body, from_number=None):
        """Send SMS"""
        try:
            message = self.client.messages.create(
                body=message_body,
                from_=from_number or self.from_number,
                to=to_number
            )
            
            return {
                'success': True,
                'message_sid': message.sid,
                'status': message.status
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_message_status(self, message_sid):
        """Get SMS delivery status"""
        try:
            message = self.client.messages(message_sid).fetch()
            return {
                'success': True,
                'status': message.status,
                'error_code': message.error_code,
                'error_message': message.error_message
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
