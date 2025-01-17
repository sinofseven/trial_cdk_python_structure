SHELL = /usr/bin/env bash -xeuo pipefail

format: \
	fmt-cdk \
	fmt-python

fmt-cdk:
	npm run format

fmt-python: \
	fmt-python-isort \
	fmt-python-black

fmt-python-isort:
	poetry run isort src/ tests/unit/

fmt-python-black:
	poetry run black src/ tests/unit/

lint: \
	lint-cdk \
	lint-python

lint-cdk:
	npm run lint

lint-python: \
	lint-python-isort \
	lint-python-black \
	lint-python-flake8

lint-python-isort:
	poetry run isort --check src/ tests/unit/

lint-python-black:
	poetry run black --check src/ tests/unit/

lint-python-flake8:
	poetry run flake8 src/ tests/unit/

module-export: \
	module-export-common

module-export-common:
	mkdir -p layers/common
	poetry export --with common_layer --without main > layers/common/requirements.txt

deploy:
	npx cdk deploy

test-unit:
	AWS_ACCESS_KEY=dummy \
	AWS_SECRET_ACCESS_KEY=dummy \
	AWS_DEFAULT_REGION=ap-northeast-1 \
	PYTHONPATH=src \
	poetry run pytest -vv tests/unit

.PHONY: \
	format \
	fmt-cdk \
	fmt-python \
	fmt-python-isort \
	fmt-python-black \
	lint \
	lint-cdk \
	lint-python \
	lint-python-isort \
	lint-python-black \
	lint-python-flake8 \
	module-export \
	module-export-common \
	deploy
