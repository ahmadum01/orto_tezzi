local_up:
	docker-compose build --parallel
	docker-compose up --attach web --attach db

local_down:
	docker-compose down

local_shell:
	docker-compose exec web sh

test:
	docker-compose run --rm web sh -c "pytest"

local_migrate:
	docker-compose  exec web python manage.py migrate

local_make_migration:
	docker-compose -f docker-compose.local.yml exec web python manage.py makemigrations

local_create_superuser:
	docker-compose -f docker-compose.local.yml exec web python manage.py createsuperuser

local_django_shell:
	docker-compose  -f docker-compose.local.yml exec web python manage.py shell

format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120
