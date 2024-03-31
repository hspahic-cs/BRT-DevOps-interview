#!/bin/bash
cd /app/

echo "$DJANGO_SUPERUSER_USERNAME"
echo "$DJANGO_SUPERUSER_EMAIL"
/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --noinput || true