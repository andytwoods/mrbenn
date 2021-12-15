#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

def update_piptools():
    for py_ver in ['3.6', '3.7', '3.8', '3.9', '3.10']:
        subprocess.run(
            [
                "py",
                "-" + py_ver,
                "-m",
                "pip",
                "install",
                "pip-tools",
            ],
            check=True,
            capture_output=True,
        )
        print(f'updated piptools for python {py_ver}')

if __name__ == "__main__":
    update_piptools()
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    # os.environ.pop("PIP_REQUIRE_VIRTUALENV")
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    subprocess.run(
        [
            "py", "-3.6",
            *common_args,
            "-P",
            "Django>=2.2,<3",
            "-o",
            "py36-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.6",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py36-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.6",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-o",
            "py36-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.6",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py36-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.7",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py37-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.7",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py37-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.7",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-o",
            "py37-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.7",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py37-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.8",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py38-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.8",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py38-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.8",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-o",
            "py38-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.8",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py38-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.8",
            *common_args,
            "-P",
            "Django>=4.0a1,<4.1",
            "-o",
            "py38-django40.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.9",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py39-django22.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.9",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py39-django30.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.9",
            *common_args,
            "-P",
            "Django>=3.1a1,<3.2",
            "-o",
            "py39-django31.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.9",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py39-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.9",
            *common_args,
            "-P",
            "Django>=4.0a1,<4.1",
            "-o",
            "py39-django40.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.10",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-o",
            "py310-django32.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "py", "-3.10",
            *common_args,
            "-P",
            "Django>=4.0a1,<4.1",
            "-o",
            "py310-django40.txt",
        ],
        check=True,
        capture_output=True,
    )