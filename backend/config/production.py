"""
Production settings for deployment
"""
from .settings import *
import dj_database_url
import os

# Security
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# Database - Use PostgreSQL in production
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Whitenoise middleware (add at position 1, right after SecurityMiddleware)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# CORS for production
CORS_ALLOWED_ORIGINS = [
    os.environ.get('ADMIN_FRONTEND_URL', 'http://localhost:5173'),
    os.environ.get('STORE_FRONTEND_URL', 'http://localhost:3000'),
]

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Encryption key from environment
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', ENCRYPTION_KEY)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
