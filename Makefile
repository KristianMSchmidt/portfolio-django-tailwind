# Run local development server
runserver:
	pipenv run python manage.py runserver

# Deploy on Linode with Gunicorn
check-deploy:
	pipenv run python manage.py check --deploy

# Run test suite
test:
	pipenv run python manage.py test

# start tailwind
tailwind-start:
	pipenv run python manage.py tailwind start

# build minified production tailwind css
tailwind-build:
	pipenv run python manage.py tailwind build

