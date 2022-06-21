.PHONY: up build down build-jupyter jupyter build-python-dev \
	format lint unit-tests clean-docker clean-python

up: build
	docker-compose up

build:
	docker-compose build

down:
	docker-compose down --remove-orphans

# below commands could be modularized further but it's not the point of the challenge
build-jupyter:
	docker-compose -f docker-compose.jupyter.yaml build

# NOTE: keep as `docker-compose up`
# you cannot reach Jupyter via browser with `docker-compose run jupyter`
jupyter: build-jupyter
	docker-compose -f docker-compose.jupyter.yaml up

build-python-dev:
	docker-compose -f docker-compose.python-dev.yaml build

format: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run format

lint: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run lint

unit-tests: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run unit-tests

clean-docker: down
	docker system prune -f

clean-python:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf .pytest_cache
	find . -name '.eggs' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
