"""
API Integrations URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'providers', views.APIProviderViewSet, basename='api-providers')
router.register(r'configurations', views.APIConfigurationViewSet, basename='api-configurations')

urlpatterns = [
    path('', include(router.urls)),
]
