"""
Management command to load initial API providers
"""
from django.core.management.base import BaseCommand
from apps.api_integrations.models import APIProvider


class Command(BaseCommand):
    help = 'Load initial API providers into database'

    def handle(self, *args, **options):
        providers = [
            # Payment Providers
            {
                'name': 'Stripe',
                'slug': 'stripe',
                'category': 'payment',
                'description': 'Accept payments online with Stripe',
                'required_fields': ['api_key'],
                'optional_fields': ['webhook_secret'],
                'is_active': True
            },
            {
                'name': 'PayPal',
                'slug': 'paypal',
                'category': 'payment',
                'description': 'PayPal payment gateway',
                'required_fields': ['client_id', 'client_secret'],
                'optional_fields': [],
                'is_active': True
            },
            {
                'name': 'Razorpay',
                'slug': 'razorpay',
                'category': 'payment',
                'description': 'Indian payment gateway',
                'required_fields': ['api_key', 'api_secret'],
                'optional_fields': [],
                'is_active': True
            },
            
            # Email Providers
            {
                'name': 'SendGrid',
                'slug': 'sendgrid',
                'category': 'email',
                'description': 'Email delivery service',
                'required_fields': ['api_key'],
                'optional_fields': ['from_email', 'from_name'],
                'is_active': True
            },
            {
                'name': 'Mailgun',
                'slug': 'mailgun',
                'category': 'email',
                'description': 'Email API service',
                'required_fields': ['api_key', 'domain'],
                'optional_fields': [],
                'is_active': True
            },
            
            # SMS Providers
            {
                'name': 'Twilio',
                'slug': 'twilio',
                'category': 'sms',
                'description': 'SMS and WhatsApp messaging',
                'required_fields': ['account_sid', 'auth_token'],
                'optional_fields': ['from_number'],
                'is_active': True
            },
            
            # Shipping Providers
            {
                'name': 'FedEx',
                'slug': 'fedex',
                'category': 'shipping',
                'description': 'FedEx shipping and tracking',
                'required_fields': ['api_key', 'password', 'account_number'],
                'optional_fields': [],
                'is_active': True
            },
            {
                'name': 'UPS',
                'slug': 'ups',
                'category': 'shipping',
                'description': 'UPS shipping and tracking',
                'required_fields': ['username', 'password', 'access_key'],
                'optional_fields': [],
                'is_active': True
            },
            {
                'name': 'DHL',
                'slug': 'dhl',
                'category': 'shipping',
                'description': 'DHL Express shipping',
                'required_fields': ['api_key', 'api_secret'],
                'optional_fields': [],
                'is_active': True
            },
        ]
        
        created_count = 0
        updated_count = 0
        
        for provider_data in providers:
            provider, created = APIProvider.objects.update_or_create(
                slug=provider_data['slug'],
                defaults=provider_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {provider.name}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'↻ Updated: {provider.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSummary: {created_count} created, {updated_count} updated'))
