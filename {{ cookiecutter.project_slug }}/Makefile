PROJECT_NAME={{ cookiecutter.project_slug }}
VENV_DIR=./venv

.PHONY: venv
venv:
	rm -rf ${VENV_DIR}
	python3 -m venv --prompt ${PROJECT_NAME} --upgrade-deps ${VENV_DIR}

{% if cookiecutter.create_dockerfile == "yes" or cookiecutter.create_dockerfile == "y" -%}
.PHONY: docker_build
docker_build:
	docker build -t ${PROJECT_NAME} .

{% endif -%}
.PHONY: dependencies
dependencies:
	${VENV_DIR}/bin/pip install -e .

.PHONY: deps
deps: dependencies

.PHONY: setup
setup: venv deps
