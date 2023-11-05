# {{ cookiecutter.project_slug }}

## Usage

All task files are stored in [{{ cookiecutter.package_name }}](./{{ cookiecutter.package_name }}).

### Local Development Setup

Set up the virtual environment and install dependencies:

```shell
make setup
```

Activate the virtual environment:

```shell
# Activate the virtualenv
source ./venv/bin/activate
rcmt version
```

### Add a new dependency

1.  Add the dependency to [`pyproject.toml`](./pyproject.toml):
    ```toml
    # ...
    dependencies = [
      "rcmt=={{ cookiecutter._rcmt_version }}",
      "<Python package>==<version>"
    ]
    # ...
    ```
2.  Install dependencies
    ```shell
    make deps
    ```
{% if cookiecutter.create_dockerfile == "yes" or cookiecutter.create_dockerfile == "y" %}
### Build the Docker Image

```shell
make docker_build
```
{%- endif %}
