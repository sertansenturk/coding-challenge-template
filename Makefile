.PHONY: api post build-api down-api \
	app build-app down-app \
	build-jupyter jupyter down-jupyter \
	build-python-dev format lint unit-tests \
	clean-docker clean-python

QUERY=some dummy message

down: down-api down-app down-jupyter down-python-dev

api: build-api
	docker-compose -f docker-compose.api.yaml up

post:
	curl -X POST localhost:5000/dummy -d '$(QUERY)' -w "\n"

build-api:
	docker-compose -f docker-compose.api.yaml build

down-api:
	docker-compose -f docker-compose.api.yaml down --remove-orphans

app: build-app
	docker-compose -f docker-compose.app.yaml up

build-app:
	docker-compose -f docker-compose.app.yaml build

down-app:
	docker-compose -f docker-compose.app.yaml down --remove-orphans

# below commands could be modularized further but it's not the point of the challenge
build-jupyter:
	docker-compose -f docker-compose.jupyter.yaml build

# NOTE: keep as `docker-compose up`
# you cannot reach Jupyter via browser with `docker-compose run jupyter`
jupyter: build-jupyter
	docker-compose -f docker-compose.jupyter.yaml up

down-jupyter:
	docker-compose -f docker-compose.jupyter.yaml down --remove-orphans

build-python-dev:
	docker-compose -f docker-compose.python-dev.yaml build

down-python-dev:
	docker-compose -f docker-compose.python-dev.yaml down --remove-orphans

format: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run format

lint: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run lint

unit-tests: build-python-dev
	docker-compose -f docker-compose.python-dev.yaml run unit-tests

clean-docker: down
	docker rmi $$(docker images --filter "dangling=true" -q --no-trunc)

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
