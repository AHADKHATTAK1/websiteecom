from .settings import *
import os

# SECURITY
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'CHANGE-THIS-IN-PRODUCTION')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Database - PostgreSQL for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'ecommerce_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CORS
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')

# CSRF Trusted Origins (CRITICAL for Railway deployment)
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-615d5.up.railway.app',
    'https://*.railway.app',
    'https://websiteecom-six.vercel.app',
    'https://websiteecom.vercel.app',
]


# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
