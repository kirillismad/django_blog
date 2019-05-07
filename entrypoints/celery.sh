#!/bin/bash

set -e 
celery -A blog worker -l info --pidfile=/celery/celery_%n.pid