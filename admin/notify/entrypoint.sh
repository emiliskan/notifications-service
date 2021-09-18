#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z "$DJANGO_POSTGRES_HOST" "$DJANGO_POSTGRES_PORT"; do
  sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn config.wsgi --bind 0.0.0.0:8000
exec "$@"