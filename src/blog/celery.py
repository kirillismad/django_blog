import os
from celery import Celery
from celery.schedules import crontab

assert 'DJANGO_SETTINGS_MODULE' in os.environ

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'background_task': {
        'task': 'main.tasks.background_task',
        'schedule': crontab()
    }
}
