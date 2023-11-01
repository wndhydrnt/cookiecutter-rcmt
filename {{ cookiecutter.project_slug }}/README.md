# {{ cookiecutter.project_slug }}

## Usage

All task files are stored in [{{ cookiecutter.package_name }}](./{{ cookiecutter.package_name }}).

### Run rcmt locally

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
      "rcmt==0.26.0",
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
