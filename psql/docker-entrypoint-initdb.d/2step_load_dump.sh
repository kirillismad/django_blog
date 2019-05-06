#!/bin/bash

set -e

psql -f /dump.sql django_blog > /dev/null