from rest_framework import serializers
from .models import ThemeSettings

class ThemeSettingsSerializer(serializers.ModelSerializer):
    """Theme settings serializer"""
    class Meta:
        model = ThemeSettings
        fields = '__all__'
