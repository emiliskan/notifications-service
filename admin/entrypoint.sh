#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py collectstatic --no-input
python manage.py migrate

gunicorn --bind 0.0.0.0:8001 --reload -w 4 config.wsgi:application
