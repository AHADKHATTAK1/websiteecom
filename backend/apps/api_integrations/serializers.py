"""
API Integrations serializers
"""
from rest_framework import serializers
from .models import APIProvider, APIConfiguration, APILog


class APIProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIProvider
        fields = '__all__'


class APIConfigurationSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name', read_only=True)
    api_key_set = serializers.SerializerMethodField()
    
    class Meta:
        model = APIConfiguration
        fields = ['id', 'provider', 'provider_name', 'is_active', 'is_test_mode',
                  'endpoint_url', 'configuration', 'last_tested_at', 'test_status',
                  'test_message', 'api_key_set', 'created_at', 'updated_at']
        read_only_fields = ['id', 'last_tested_at', 'test_status', 'test_message',
                           'created_at', 'updated_at']
    
    def get_api_key_set(self, obj):
        return bool(obj.api_key)


class APIConfigurationCreateSerializer(serializers.ModelSerializer):
    raw_api_key = serializers.CharField(write_only=True)
    raw_api_secret = serializers.CharField(write_only=True, required=False, allow_blank=True)
    
    class Meta:
        model = APIConfiguration
        fields = ['provider', 'raw_api_key', 'raw_api_secret', 'endpoint_url',
                  'configuration', 'is_active', 'is_test_mode']
    
    def create(self, validated_data):
        raw_api_key = validated_data.pop('raw_api_key')
        raw_api_secret = validated_data.pop('raw_api_secret', '')
        
        instance = APIConfiguration(**validated_data)
        instance.set_api_key(raw_api_key)
        if raw_api_secret:
            instance.set_api_secret(raw_api_secret)
        instance.save()
        
        return instance


class APILogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APILog
        fields = ['id', 'endpoint', 'method', 'status_code', 'response_time',
                  'is_error', 'error_message', 'created_at']
        read_only_fields = fields
