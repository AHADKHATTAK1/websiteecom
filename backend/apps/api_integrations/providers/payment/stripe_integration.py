"""
Stripe Payment Integration
"""
import stripe
from apps.api_integrations.api_manager import BaseAPIManager



class StripeIntegration(BaseAPIManager):
    """Stripe payment processing"""
    
    def __init__(self, configuration):
        super().__init__(configuration)
        stripe.api_key = self.api_key
    
    def _get_auth_headers(self):
        return {'Authorization': f'Bearer {self.api_key}'}
    
    def test_connection(self):
        """Test Stripe API connection"""
        try:
            # Try to retrieve account details
            account = stripe.Account.retrieve()
            return {
                'success': True,
                'message': f'Connected to Stripe account: {account.get("id")}',
                'account_name': account.get('business_profile', {}).get('name', 'N/A')
            }
        except stripe.error.AuthenticationError:
            return {
                'success': False,
                'message': 'Invalid API key'
            }
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
    
    def create_payment_intent(self, amount, currency='usd', metadata=None):
        """Create a payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency,
                metadata=metadata or {}
            )
            return {
                'success': True,
                'client_secret': intent.client_secret,
                'payment_intent_id': intent.id
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def create_customer(self, email, name=None, metadata=None):
        """Create a Stripe customer"""
        try:
            customer = stripe.Customer.create(
                email=email,
                name=name,
                metadata=metadata or {}
            )
            return {
                'success': True,
                'customer_id': customer.id
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def refund_payment(self, payment_intent_id, amount=None):
        """Refund a payment"""
        try:
            refund = stripe.Refund.create(
                payment_intent=payment_intent_id,
                amount=int(amount * 100) if amount else None
            )
            return {
                'success': True,
                'refund_id': refund.id,
                'status': refund.status
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
