runscript:
	python3 main.py

lint:
	poetry run flake8 main.py

test:
	poetry run pytest --cov=main --cov-report=xml

install:
	poetry install