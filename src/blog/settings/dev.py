# noinspection PyUnresolvedReferences
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'db_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# MEMCACHE_HOST = 'localhost'
# MEMCACHE_PORT = '11211'
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': f'{MEMCACHE_HOST}:{MEMCACHE_PORT}',
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

BROKER_USER = 'broker_user'
BROKER_PASSWORD = 'password123'
BROKER_HOST = 'localhost'
BROKER_PORT = '5672'
CELERY_BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/'
