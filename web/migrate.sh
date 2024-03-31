#!/bin/bash
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_EMAIL:-"test@notneeded.com"}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput || true