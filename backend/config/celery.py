import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
app = Celery("digital_shop")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()