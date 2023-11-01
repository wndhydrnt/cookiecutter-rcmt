# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
import os.path
import platform
import sys
import urllib.request


def is_python() -> bool:
    if sys.version_info.major < 3:
        return False

    if sys.version_info.minor < 9:
        return False

    return True


def set_python_version_variable() -> None:
    data = _read_cookiecutter_json()
    data["_python_version"] = platform.python_version()
    _write_cookiecutter_json(data)


def set_latest_rcmt_version() -> None:
    try:
        with urllib.request.urlopen("https://pypi.org/pypi/rcmt/json") as f:
            package_data = json.load(f)

        data = _read_cookiecutter_json()
        data["_rcmt_version"] = package_data["version"]
        _write_cookiecutter_json(data)
    except Exception:
        pass


def _read_cookiecutter_json() -> dict:
    cookiecutter_json_path = os.path.join(os.getcwd(), "cookiecutter.json")
    with open(file=cookiecutter_json_path, mode="r") as f:
        return json.load(f)


def _write_cookiecutter_json(data: dict) -> None:
    cookiecutter_json_path = os.path.join(os.getcwd(), "cookiecutter.json")
    with open(file=cookiecutter_json_path, mode="w") as f:
        json.dump(data, fp=f)


if __name__ == "__main__":
    success = is_python()
    if success is False:
        print(
            f"ERROR: rcmt requires at least Python version 3.9 (current: {platform.python_version()}) - please update Python",
            file=sys.stderr,
        )
        sys.exit(1)

    set_python_version_variable()
