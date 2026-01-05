"""
URLs for HTML admin dashboard
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('theme/', views.get_theme_settings, name='get_theme'),
    path('theme/update/', views.update_theme_settings, name='update_theme'),
    path('theme/presets/', views.list_theme_presets, name='list_presets'),
    path('theme/apply-preset/', views.apply_theme_preset, name='apply_preset'),
    path('theme/upload/', views.upload_theme_image, name='upload_image'),
]
