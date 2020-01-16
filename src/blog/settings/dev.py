# noinspection PyUnresolvedReferences
from .base import *

from os import environ as env

DEBUG = True

SECRET_KEY = env.get('SECRET_KEY', '7txt(s51fq2z4&fgd)3@hewq!!$i*)r$si5=o$p8&l96$ybgph')

TMP_DIR = pathlib.Path('/tmp')
MEDIA_ROOT = TMP_DIR.joinpath('media_root')
STATIC_ROOT = TMP_DIR.joinpath('static_root')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('POSTGRES_DB', 'db'),
        'USER': env.get('POSTGRES_USER', 'db_user'),
        'PASSWORD': env.get('POSTGRES_PASSWORD', 'password123'),
        'HOST': env.get('POSTGRES_HOST', 'localhost'),
        'PORT': env.get('POSTGRES_PORT', '5432'),
    }
}


CACHE_HOST = env.get('CACHE_HOST', 'localhost')
CACHE_PORT = env.get('CACHE_PORT', '11211')

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': f'{CACHE_HOST}:{CACHE_PORT}',
        'TIMEOUT': 5,
    }
}

BROKER_USER = env.get('BROKER_USER', 'broker_user')
BROKER_PASSWORD = env.get('BROKER_PASSWORD', 'password123')
BROKER_HOST = env.get('BROKER_HOST', 'localhost')
BROKER_PORT = env.get('BROKER_PORT', '5672')
CELERY_BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/'
