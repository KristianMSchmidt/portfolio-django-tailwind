# Run local development server
runserver:
	pipenv run python manage.py runserver

# Run production server locally
gunicorn:
	pipenv run gunicorn config.wsgi --log-file-

# Deployment checklist 
checksecurity:
	heroku run python manage.py check --deploy

# Run test suite
test:
	pipenv run python manage.py test

# start tailwind
tailwind-start:
	pipenv run python manage.py tailwind start

# build minified production tailwind css
tailwind-build:
	pipenv run python manage.py tailwind build

# makemigrations
migrations:
	pipenv run python manage.py makemigrations

# migrate
migrate:
	pipenv run python manage.py migrate

# build production tailwind css and push master branch to heroku
make push-heroku:
	pipenv run python manage.py tailwind build
	git push heroku master

# pipenv install package --pre (because of black in prelease)