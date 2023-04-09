lint:
	# Shows strange error in blockchain.py which I do not know how to fix
	# EXTERNAL_SERVICES_DISABLED=yes mypy .
	flake8 . --count --show-source --statistics --max-line-length 120
	isort --check .
	black --check .

format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120

local_up:
	docker-compose build --parallel
	docker-compose up --attach web --attach db

local_down:
	docker-compose down

local_shell:
	docker-compose exec web sh

test:
	docker-compose run --rm web sh -c "pytest"

local_django_shell:
	docker-compose  -f docker-compose.local.yml exec web python manage.py shell
