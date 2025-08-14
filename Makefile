install:
	uv sync

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

run:
	uv run python manage.py runserver

render-start:
	uv run gunicorn task_manager.wsgi

build:
	./build.sh

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test:
	uv run pytest --ds=task_manager.settings --reuse-db

coverage:
	uv run coverage run -m pytest --ds=task_manager.settings
	uv run coverage report

ci-install:
	uv sync --group dev

ci-migrate:
	uv run python manage.py makemigrations --noinput && \
	uv run python manage.py migrate --noinput

ci-test:
	uv run coverage run -m pytest --ds=task_manager.settings --reuse-db
	uv run coverage xml
