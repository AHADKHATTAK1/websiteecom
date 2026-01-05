"""
API Integration Models
"""
from django.db import models
from django.contrib.auth import get_user_model
from core.base_models import TimeStampedModel
from utils.encryption import encryption_service

User = get_user_model()


class APIProvider(TimeStampedModel):
    """Catalog of available API providers"""
    
    CATEGORY_CHOICES = [
        ('payment', 'Payment'),
        ('shipping', 'Shipping'),
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('ai', 'Artificial Intelligence'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    logo = models.ImageField(upload_to='api_logos/', null=True, blank=True)
    documentation_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    # Configuration schema (defines what fields are required)
    required_fields = models.JSONField(default=list)  # ['api_key', 'api_secret', 'endpoint_url']
    optional_fields = models.JSONField(default=list)
    
    class Meta:
        db_table = 'api_providers'
        verbose_name = 'API Provider'
        verbose_name_plural = 'API Providers'
    
    def __str__(self):
        return f"{self.name} ({self.category})"


class APIConfiguration(TimeStampedModel):
    """User's API configurations with encrypted keys"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_configurations')
    provider = models.ForeignKey(APIProvider, on_delete=models.CASCADE)
    
    # Encrypted fields
    api_key = models.TextField()  # Encrypted
    api_secret = models.TextField(blank=True)  # Encrypted
    
    # Configuration
    endpoint_url = models.URLField(blank=True)
    configuration = models.JSONField(default=dict)  # Extra settings
    
    # Status
    is_active = models.BooleanField(default=True)
    is_test_mode = models.BooleanField(default=True)
    last_tested_at = models.DateTimeField(null=True, blank=True)
    test_status = models.CharField(max_length=20, default='not_tested')  # success, failed, not_tested
    test_message = models.TextField(blank=True)
    
    class Meta:
        db_table = 'api_configurations'
        unique_together = ['user', 'provider']
        verbose_name = 'API Configuration'
        verbose_name_plural = 'API Configurations'
    
    def __str__(self):
        return f"{self.user.email} - {self.provider.name}"
    
    def set_api_key(self, raw_key):
        """Encrypt and set API key"""
        self.api_key = encryption_service.encrypt(raw_key)
    
    def get_api_key(self):
        """Decrypt and get API key"""
        return encryption_service.decrypt(self.api_key)
    
    def set_api_secret(self, raw_secret):
        """Encrypt and set API secret"""
        self.api_secret = encryption_service.encrypt(raw_secret)
    
    def get_api_secret(self):
        """Decrypt and get API secret"""
        return encryption_service.decrypt(self.api_secret)


class APILog(TimeStampedModel):
    """Log all API calls for monitoring"""
    
    configuration = models.ForeignKey(APIConfiguration, on_delete=models.CASCADE, related_name='logs')
    
    # Request details
    endpoint = models.CharField(max_length=500)
    method = models.CharField(max_length=10)  # GET, POST, PUT, DELETE
    request_data = models.JSONField(default=dict)
    request_headers = models.JSONField(default=dict)
    
    # Response details
    response_data = models.JSONField(default=dict)
    response_headers = models.JSONField(default=dict)
    status_code = models.IntegerField(null=True)
    response_time = models.FloatField(help_text='Response time in seconds')
    
    # Error handling
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)
    error_type = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = 'api_logs'
        verbose_name = 'API Log'
        verbose_name_plural = 'API Logs'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['configuration', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.configuration.provider.name} - {self.method} {self.endpoint}"
