#!/bin/bash
APP_PORT=${PORT:-8080}

cd /app
/opt/venv/bin/python manage.py createsuperuser --noinput || true
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm BRT_DevOps_Interview.wsgi:application --bind "0.0.0.0:${APP_PORT}"