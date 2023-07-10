run:
	python manage.py runserver

makemigrate:
	python manage.py makemigrations

migrate:
	python manage.py migrate

lint:
	lint ./*
