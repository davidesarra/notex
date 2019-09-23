install:
	pip install --upgrade pip &&\
	pip install -e .[dev]

format:
	black .

lint:
	flake8

test:
	black --check --diff . &&\
	flake8 &&\
	pytest -v
