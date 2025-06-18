#!/bin/sh

# # Apply migrations
# python python manage.py collectstatic

# python manage.py migrate

# Start Gunicorn server

python manage.py seed_projects
python manage.py seed_checkouts
gunicorn mockapi.wsgi:application --bind 0.0.0.0:8000