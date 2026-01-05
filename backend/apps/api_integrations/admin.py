"""
Admin configuration for API integrations
"""
from django.contrib import admin
from .models import APIProvider, APIConfiguration, APILog


@admin.register(APIProvider)
class APIProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['category', 'name']


@admin.register(APIConfiguration)
class APIConfigurationAdmin(admin.ModelAdmin):
    list_display = ['user', 'provider', 'is_active', 'is_test_mode', 'test_status', 'last_tested_at']
    list_filter = ['is_active', 'is_test_mode', 'test_status', 'provider__category']
    search_fields = ['user__email', 'provider__name']
    readonly_fields = ['last_tested_at', 'test_status', 'test_message', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Configuration', {'fields': ('user', 'provider', 'is_active', 'is_test_mode')}),
        ('API Credentials', {'fields': ('api_key', 'api_secret', 'endpoint_url', 'configuration')}),
        ('Testing', {'fields': ('test_status', 'test_message', 'last_tested_at')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ['configuration', 'method', 'endpoint', 'status_code', 'response_time', 'is_error', 'created_at']
    list_filter = ['is_error', 'method', 'created_at']
    search_fields = ['endpoint', 'error_message']
    readonly_fields = ['configuration', 'endpoint', 'method', 'request_data', 'response_data', 
                       'status_code', 'response_time', 'is_error', 'error_message', 'created_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
