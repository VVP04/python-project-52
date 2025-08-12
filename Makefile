install:
	uv sync

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

run:
	python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

build:
	./build.sh

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test:
	pytest --ds=task_manager.settings --reuse-db

coverage:
	coverage run -m pytest --ds=task_manager.settings
	coverage report