#!/bin/bash

set -e

celery -A blog beat -s /celery/celerybeat-schedule --pidfile=/celery/celerybeat_%n.pid