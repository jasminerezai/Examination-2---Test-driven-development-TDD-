.PHONY: test coverage install

install:
	pip install -r requirements.txt

test:
	pytest -v

flake8:
	flake8 src/

docstring:
	pdoc --html src