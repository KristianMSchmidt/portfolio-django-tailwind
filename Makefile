# Run local development server
runserver:
	pipenv run python manage.py runserver

# Deploy on Linode with Gunicorn
deploy:
	pipenv clean
	pipenv sync
	pipenv run python manage.py collectstatic --noinput
	pipenv run python manage.py migrate
	pipenv run python ~/repos/portfolio-django-tailwind-linode/manage.py check --deploy
	pipenv run gunicorn config.wsgi -b 0.0.0.0:8000

# Run test suite
test:
	pipenv run python manage.py test

# start tailwind
tailwind-start:
	pipenv run python manage.py tailwind start

# build minified production tailwind css
tailwind-build:
	pipenv run python manage.py tailwind build

