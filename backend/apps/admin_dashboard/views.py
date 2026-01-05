"""
Django views for HTML admin interface (No React needed)
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import ThemeSettings
from .serializers import ThemeSettingsSerializer

def index(request):
    """Dashboard home"""
    return render(request, 'admin_dashboard/index.html')

@api_view(['GET'])
@permission_classes([AllowAny]) # Store needs this without auth
def get_theme_settings(request):
    """Get active theme settings"""
    theme = ThemeSettings.objects.filter(is_active=True).first()
    if not theme:
        # Create default if none exists
        theme = ThemeSettings.objects.create(site_name="My AI Store")
    
    serializer = ThemeSettingsSerializer(theme)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def update_theme_settings(request):
    """Update theme settings (Admin only)"""
    if request.user.role != 'admin':
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        
    theme = ThemeSettings.objects.filter(is_active=True).first()
    serializer = ThemeSettingsSerializer(theme, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_theme_presets(request):
    """List all available theme presets"""
    from .theme_presets import list_presets
    presets = list_presets()
    return Response(presets)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_theme_preset(request):
    """Apply a theme preset"""
    if request.user.role != 'admin':
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
    preset_id = request.data.get('preset_id')
    if not preset_id:
        return Response({'error': 'preset_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    from .theme_presets import get_preset
    preset = get_preset(preset_id)
    
    if not preset:
        return Response({'error': 'Preset not found'}, status=status.HTTP_404_NOT_FOUND)
    
    theme = ThemeSettings.objects.filter(is_active=True).first()
    if not theme:
        theme = ThemeSettings.objects.create(is_active=True)
    
    # Apply preset settings
    for key, value in preset['settings'].items():
        setattr(theme, key, value)
    
    theme.save()
    serializer = ThemeSettingsSerializer(theme)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_theme_image(request):
    """Upload logo or banner image"""
    if request.user.role != 'admin':
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
    image_type = request.data.get('type')  # 'logo' or 'banner'
    image_file = request.FILES.get('file')
    
    if not image_type or not image_file:
        return Response({'error': 'type and file are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    theme = ThemeSettings.objects.filter(is_active=True).first()
    if not theme:
        theme = ThemeSettings.objects.create(is_active=True)
    
    if image_type == 'logo':
        theme.logo = image_file
    elif image_type == 'banner':
        theme.banner_image = image_file
    else:
        return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)
    
    theme.save()
    serializer = ThemeSettingsSerializer(theme)
    return Response(serializer.data)


@login_required
def api_config(request):
    """API configuration page"""
    return render(request, 'admin/api_config.html')


@login_required
def ai_config(request):
    """AI chatbot configuration page"""
    return render(request, 'admin/ai_config.html')


@login_required
def products_list(request):
    """Products listing page"""
    return render(request, 'admin/products.html')


@login_required
def orders_list(request):
    """Orders listing page"""
    return render(request, 'admin/orders.html')
