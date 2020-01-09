#!/bin/sh

set -e

python manage.py collectstatic --no-input
# python manage.py migrate --no-input

gunicorn --bind 0.0.0.0:8000 --workers 1 --timeout 30 --graceful-timeout 30 blog.wsgi:application
