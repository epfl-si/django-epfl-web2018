PYTHON_VERSION=3.14.4
PYTHON_VENV=django-epfl-web2018

.PHONY: help
help: ## Display this help message.
	@echo "Please use make <target> where <target> is one of"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-15s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Remove coverage reports and build artifacts.
	@rm -fr htmlcov/
	@rm -f coverage.xml .coverage
	@rm -fr .pdm-build/
	@rm -fr dist/

.PHONY: cleanall
cleanall: clean ## Remove coverage reports, build artifacts, venv and tox envs.
	@rm -fr .tox/
	@pyenv virtualenv-delete --force ${PYTHON_VENV}
	@rm -f .python-version

.PHONY: lint
lint: ## Check coding style.
	tox -e lint

.PHONY: test
test: ## Run tests on every supported Python/Django combination.
	tox

.PHONY: installdeps
installdeps: ## Install all necessary dependencies in the virtualenv.
	@eval "$$(pyenv init -)" && pyenv activate ${PYTHON_VENV} && \
	pip install -r requirements/requirements-tools.txt && \
	pip install -r requirements/requirements-lint.txt && \
	pip install -r requirements/requirements-dev.txt && \
	pip install .

.PHONY: venv
venv: ## Create a virtualenv django-epfl-web2018 with pyenv.
	@if [ ! -d "${HOME}/.pyenv/versions/${PYTHON_VERSION}" ]; then \
		pyenv install ${PYTHON_VERSION}; \
	fi
	@pyenv virtualenv ${PYTHON_VERSION} ${PYTHON_VENV}

.PHONY: setup
setup: venv installdeps ## Setup a virtualenv and install dependencies.
	@echo ${PYTHON_VENV} > .python-version
