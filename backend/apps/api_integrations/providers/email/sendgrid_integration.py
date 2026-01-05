"""
SendGrid Email Integration
"""
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from apps.api_integrations.api_manager import BaseAPIManager



class SendGridIntegration(BaseAPIManager):
    """SendGrid email service integration"""
    
    def __init__(self, configuration):
        super().__init__(configuration)
        self.client = SendGridAPIClient(self.api_key)
        self.from_email = self.extra_config.get('from_email', '')
    
    def _get_auth_headers(self):
        return {'Authorization': f'Bearer {self.api_key}'}
    
    def test_connection(self):
        """Test SendGrid connection"""
        try:
            response = self.client.client.api_keys._(self.api_key.split('.')[-1]).get()
            return {
                'success': True,
                'message': 'SendGrid connection successful'
            }
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
    
    def send_email(self, to_email, subject, html_content, from_email=None):
        """Send an email"""
        try:
            message = Mail(
                from_email=from_email or self.from_email,
                to_emails=to_email,
                subject=subject,
                html_content=html_content
            )
            
            response = self.client.send(message)
            
            return {
                'success': True,
                'status_code': response.status_code,
                'message_id': response.headers.get('X-Message-Id')
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def send_template_email(self, to_email, template_id, dynamic_data):
        """Send email using template"""
        try:
            message = Mail(from_email=self.from_email, to_emails=to_email)
            message.template_id = template_id
            message.dynamic_template_data = dynamic_data
            
            response = self.client.send(message)
            
            return {
                'success': True,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
