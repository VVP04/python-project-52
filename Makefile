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
	uv run ruff check --fix