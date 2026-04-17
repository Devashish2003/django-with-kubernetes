#!/bin/bash
APP_PORT=${PORT}
if [ -z "$APP_PORT" ]; then
  APP_PORT=8020  # Default if not provided
fi
cd /app

echo "Starting Django app on port $APP_PORT"
gunicorn --worker-tmp-dir /dev/shm k8s.wsgi:application --bind "0.0.0.0:${APP_PORT}"
