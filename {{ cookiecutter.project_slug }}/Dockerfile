FROM python:{{ cookiecutter._python_version }}

RUN mkdir /rcmt
COPY ./pyproject.toml /rcmt/
COPY ./{{ cookiecutter.package_name }}/__init__.py /rcmt/{{ cookiecutter.package_name }}/__init__.py
WORKDIR /rcmt
RUN pip install -e .
COPY ./{{ cookiecutter.package_name }} /rcmt/{{ cookiecutter.package_name }}
