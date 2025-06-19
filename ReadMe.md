# CIRCE

An example of how to benefit from a continuous integration workflow hosted at GitHub to control the evolutions of a simple Python project.

This project is "non-packaged", i.e. not intended to be built and distributed as a package. Goals are to
- organize code in files
- run tests
- use linters and formatters
- manage dependencies

# 1st step
- Create project repo @ Git Hub
- Clone it to dev workstation and sync from there or use codespace@github
- Collect an initial   [.gitignore file @ GitHub](https://github.com/github/gitignore/blob/main/Python.gitignore)
- Create folders for sources (src), tests (tests) and scripts (scripts)

Commit !

# 2nd step
At the root of the project, create a `pyproject.toml` file, to gather standardized (PEP 621) project metadata. Customize the template herebelow:

``
[project]
name = "my-script-project"
version = "0.1.0"
description = "Just a Python script project with tests and tools."
requires-python = ">=3.8"

[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "mypy"
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88
target-version = "py38"

[tool.mypy]
python_version = "3.8"
ignore_missing_imports = true


``
The template mentions 
- pytest for testing
- ruff for linting 
- mypy for type checking.

# 3rd step
Initiate a virtual environment for Python.

``python3 -m venv .venv``

Then, activate it (using the dialect of your OS)

``source .venv/bin/activate``

# 4th step
Populate code. Then only, run:

``pip install -e .[dev]``

This installs the dependencies needed for development.

# 5th step
Populate tests. 