lint:  ## lint fix
	black .
	isort . --profile black
	flake8 .

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations
