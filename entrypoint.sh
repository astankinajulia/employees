#!/bin/bash
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
done

SCRIPT_PATH=$(dirname "${BASH_SOURCE[0]}")

echo "Start app"

gunicorn main:make_app --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker
