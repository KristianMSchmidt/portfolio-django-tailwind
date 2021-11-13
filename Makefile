## ----------------------------------------------------------------------
## Makefile for portfolio.kristianms.com
##
## Used for both development and production. See targets below.
## ----------------------------------------------------------------------

help:   # Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)


# ---------- Development ---------- #
build:  ## Build or rebuild development docker image
	docker-compose -f docker-compose.dev.yml build

develop:  ## Run development server
	docker-compose -f docker-compose.dev.yml up --remove-orphans

shell:  ## Open shell in running docker development container
	docker-compose -f docker-compose.dev.yml exec web /bin/bash

tailwind-start:  ## start tailwind (should be running while developing)
	docker-compose -f docker-compose.dev.yml exec web python manage.py tailwind start

tailwind-build: ## build minified production tailwind css
	docker-compose -f docker-compose.dev.yml exec web python manage.py tailwind start


# ---------- Checks and tests ---------- #
test: ## Execute tests within the docker image
	docker-compose -f docker-compose.dev.yml exec web python manage.py test


# ---------- Production ---------- #
production_stop: ## Stop production server
	docker-compose -f docker-compose.prod.yml down --remove-orphans

production_start: ## Start production server as daemon
	docker-compose -f docker-compose.prod.yml up --build --remove-orphans -d

production_djangologs: ## Show django logs
	docker logs kristianmscom_web_1

production_accesslogs: ## Show nginx access logs
	docker logs kristianmscom_nginx_1

production_shell: # Open shell in running docker production container
	docker-compose -f docker-compose.prod.yml exec web /bin/bash

