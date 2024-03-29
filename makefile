install:
	pip install --upgrade pip && \
	pip install -e .[dev]

format:
	black .

lint:
	flake8

test:
	black --check --diff . && \
	flake8 && \
	pytest -v

build-package:
	rm -rf build dist && \
	pip install --upgrade pip setuptools wheel twine && \
	python setup.py sdist bdist_wheel

test-release-package: build-package
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release-package: build-package
	git checkout master && \
	git pull origin master && \
	git tag $(shell cat setup.py | tr "\n" " " | sed -E "s/.* VERSION = \"([0-9]+\.[0-9]+\.[0-9]+)\" .*/\1/g") && \
	python -m twine upload dist/* && \
	git push origin master --tags
