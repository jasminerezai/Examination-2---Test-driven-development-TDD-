.PHONY: test coverage install

install:
	pip install -r requirements.txt

test:
	pytest -v

coverage:
<<<<<<< HEAD
	coverage run -m pytest
	coverage report -m
=======
	PYTHONPATH=. python -m coverage run -m pytest
>>>>>>> c5d9e3b663cfff4021906cf087d01261233f268d

flake8:
	flake8 proj test

# RUN MANUAL:
# make install  --- intalls packages from req.txt
# make test	    --- runs pytest
# make coverage --- runs coverage
# make flake8