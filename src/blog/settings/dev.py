# noinspection PyUnresolvedReferences
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_blog',
        'USER': 'django_blog_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# MEMCACHE_HOST = 'localhost'
# MEMCACHE_PORT = '11211'
# CACHE_MIDDLEWARE_KEY_PREFIX = 'mw'
# CACHE_MIDDLEWARE_SECONDS = 60
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': f'{MEMCACHE_HOST}:{MEMCACHE_PORT}',
#     }
# }

BROKER_USER = 'django_blog_user'
BROKER_PASSWORD = 'password123'
BROKER_HOST = 'localhost'
BROKER_PORT = '5672'
CELERY_BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/'
