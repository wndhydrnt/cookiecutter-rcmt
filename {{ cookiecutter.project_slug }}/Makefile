{% if cookiecutter.create_dockerfile == "yes" or cookiecutter.create_dockerfile == "y" -%}
DOCKER_IMAGE="{{ cookiecutter.project_slug }}"

.PHONY: docker_build
docker_build:
	docker build -t $DOCKER_IMAGE .

{% endif -%}
.PHONY: dependencies
dependencies:
	./venv/bin/pip install -e .

.PHONY: deps
deps: dependencies
