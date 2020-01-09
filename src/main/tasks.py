from celery import shared_task
from django.core import management


@shared_task
def background_task():
    print('CALL BACKGROUND TASK')
