#!/bin/sh

# Apply migrations
python python manage.py collectstatic
python manage.py migrate

# Start Gunicorn server
gunicorn mockapi.wsgi:application --bind 0.0.0.0:8000