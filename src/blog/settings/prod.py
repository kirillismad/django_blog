import os

# noinspection PyUnresolvedReferences
from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}

CACHE_HOST = os.environ['CACHE_HOST']
CACHE_PORT = os.environ['CACHE_PORT']
CACHE_MIDDLEWARE_KEY_PREFIX = os.environ['CACHE_MIDDLEWARE_KEY_PREFIX']
CACHE_MIDDLEWARE_SECONDS = os.environ['CACHE_MIDDLEWARE_SECONDS']
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
