#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py migrate


echo "${0}: collecting static files."
python manage.py collectstatic --noinput --clear

echo "${0}: running production server."
gunicorn config.wsgi -b 0.0.0.0:8000