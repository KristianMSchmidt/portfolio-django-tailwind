#!/bin/bash

set -e

echo "${0}: installing npm packages necessary to build tailwind css (only needed in development)."
python manage.py tailwind install


echo "${0}: running migrations."
python manage.py migrate


echo "${0}: collecting static files."
python manage.py collectstatic --noinput --clear


echo "${0}: Running development server."
python manage.py runserver 0.0.0.0:8000


