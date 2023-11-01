# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import os.path
import subprocess
import sys
import venv

DOCKERFILE_CREATE = "{{ cookiecutter.create_dockerfile }}"
VENV_PROMPT = "{{ cookiecutter.project_slug }}"


def create_venv() -> None:
    venv.create(
        env_dir=os.path.join(os.getcwd(), "venv"), prompt=VENV_PROMPT, with_pip=True
    )


def delete_docker_files() -> None:
    for file_name in [".dockerignore", "Dockerfile"]:
        path = os.path.join(os.getcwd(), file_name)
        os.remove(path)


def install_dependencies() -> bool:
    python_path = os.path.join(os.getcwd(), "venv", "bin", "python3")
    try:
        subprocess.run(
            args=[python_path, "-m", "pip", "install", "-e", "."],
            cwd=os.getcwd(),
        )
    except Exception:
        return False


if __name__ == "__main__":
    if DOCKERFILE_CREATE != "yes" and DOCKERFILE_CREATE != "y":
        delete_docker_files()

    create_venv()
    result = install_dependencies()
    if result is False:
        print(
            "ERROR: Failed to install rcmt and dependencies inti virtualenv",
            file=sys.stderr,
        )
        sys.exit(1)
