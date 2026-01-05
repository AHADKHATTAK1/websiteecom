"""
Celery configuration for background tasks
"""
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('ecommerce_ai')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Periodic tasks
app.conf.beat_schedule = {
    'sync-inventory-every-hour': {
        'task': 'apps.automation.tasks.sync_inventory',
        'schedule': crontab(minute=0),  # Every hour
    },
    'process-abandoned-carts': {
        'task': 'apps.automation.tasks.process_abandoned_carts',
        'schedule': crontab(minute=0, hour='*/6'),  # Every 6 hours
    },
    'generate-daily-analytics': {
        'task': 'apps.analytics.tasks.generate_daily_report',
        'schedule': crontab(minute=0, hour=0),  # Daily at midnight
    },
}
