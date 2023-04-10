.PHONY: lint
lint:
	flake8 . --count --show-source --statistics --max-line-length 120
	isort --check .
	black --check .

.PHONY: format
format:
	isort .
	black .
	flake8 . --count --show-source --statistics --max-line-length 120

.PHONY: local_up
local_up:
	docker-compose build --parallel
	docker-compose up --attach web --attach db

.PHONY: local_down
local_down:
	docker-compose down

.PHONY: local_shell
local_shell:
	docker-compose exec web sh

.PHONY: test
test:
	pytest

.PHONY: local_django_shell
local_django_shell:
	docker-compose  exec web python manage.py shell
