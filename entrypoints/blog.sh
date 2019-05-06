#!/bin/bash

set -e

/wait

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    python /src/manage.py runserver 0.0.0.0:8000
    
    elif [ "$ENV" = 'PROD' ]; then
    echo "Running Production Server"
    gunicorn -b 0.0.0.0:8000 blog.wsgi:application
    
else
    echo "Invalid ENV"
    exit 3
fi