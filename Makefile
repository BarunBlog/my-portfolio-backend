docker-build:
	docker compose up --build

docker-down:
	docker compose down

docker-start: |
	docker-down docker-build

runserver: |
	python manage.py runserver 0.0.0.0:8000

migrate_and_runserver: |
	python manage.py migrate
	python manage.py runserver 0.0.0.0:8000