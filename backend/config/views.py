from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def api_root(request):
    """API root endpoint showing available endpoints"""
    return JsonResponse(
        {
            "message": "Welcome to AI E-commerce Platform API",
            "version": "1.0",
            "endpoints": {
                "admin": "/admin/",
                "authentication": "/api/auth/",
                "products": "/api/products/",
                "orders": "/api/orders/",
                "chatbot": "/api/chatbot/",
                "integrations": "/api/integrations/",
                "analytics": "/api/analytics/",
            },
            "documentation": "/admin/",
            "status": "operational",
        }
    )
