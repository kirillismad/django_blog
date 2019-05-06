from celery import shared_task
from django.core import management


@shared_task
def rm_ghost_files():
    print('RM GHOST FILES')
    management.call_command('rm_ghost_files')
