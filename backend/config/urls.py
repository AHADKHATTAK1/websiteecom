"""
Main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import api_root

urlpatterns = [
    path("", api_root, name="api_root"),  # API welcome page
    path("admin/", admin.site.urls),
    # API endpoints
    path("api/auth/", include("apps.authentication.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/chatbot/", include("apps.ai_chatbot.urls")),
    path("api/integrations/", include("apps.api_integrations.urls")),
    path("api/automation/", include("apps.automation.urls")),
    path("api/admin-dashboard/", include("apps.admin_dashboard.urls")),
    path("api/analytics/", include("apps.analytics.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
