from celery import Celery

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mad_devs.settings')
app = Celery('main')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
