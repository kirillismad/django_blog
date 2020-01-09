import os

# noinspection PyUnresolvedReferences
from .base import *

DEBUG = False

SECRET_KEY= os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['*']

MEDIA_ROOT=pathlib.Path(os.environ['MEDIA_ROOT'])
STATIC_ROOT=pathlib.Path(os.environ['STATIC_ROOT'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
    }
}

CACHE_HOST = os.environ['CACHE_HOST']
CACHE_PORT = os.environ['CACHE_PORT']
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': f'{CACHE_HOST}:{CACHE_PORT}',
    }
}

BROKER_USER = os.environ['BROKER_USER']
BROKER_PASSWORD = os.environ['BROKER_PASSWORD']
BROKER_HOST = os.environ['BROKER_HOST']
BROKER_PORT = os.environ['BROKER_PORT']
CELERY_BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/'
