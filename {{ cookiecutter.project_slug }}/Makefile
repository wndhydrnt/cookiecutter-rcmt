{% if cookiecutter.create_dockerfile == "yes" or cookiecutter.create_dockerfile == "y" -%}
DOCKER_IMAGE={{ cookiecutter.project_slug }}
{% endif -%}
PROJECT_NAME={{ cookiecutter.project_slug }}
VENV_DIR=./venv

.PHONY: venv
venv:
	rm -rf ${VENV_DIR}
	python3 -m venv --prompt ${PROJECT_NAME} --upgrade-deps ${VENV_DIR}

{% if cookiecutter.create_dockerfile == "yes" or cookiecutter.create_dockerfile == "y" -%}
.PHONY: docker_build
docker_build:
	docker build -t ${DOCKER_IMAGE} .

{% endif -%}
.PHONY: dependencies
dependencies:
	${VENV_DIR}/bin/pip install -e .[test]

.PHONY: deps
deps: dependencies

.PHONY: setup
setup: venv deps

.PHONY: test
test:
	${VENV_DIR}/bin/pytest .
