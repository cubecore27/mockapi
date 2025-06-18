#!/bin/sh

# Run migrations first
python manage.py migrate

# Then seed data
python manage.py seed_projects
python manage.py seed_checkouts
python manage.py collectstatic --noinput
# Then start the server
gunicorn mockapi.wsgi:application --bind 0.0.0.0:8000
