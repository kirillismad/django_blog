#!/bin/sh

celery -A blog beat -s $APP_DIR/celerybeat-schedule --pidfile=