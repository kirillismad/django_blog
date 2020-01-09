#!/bin/bash

set -e

psql -U db_user -f /dump.sql db > /dev/null