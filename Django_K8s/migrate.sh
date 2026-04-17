#!/bin/bash
SUPERUSER_EMAIL=${SUPERUSER_EMAIL:-"devashish@hobbiate.com"}
cd /app/

python3 manage.py migrate --noinput
python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true