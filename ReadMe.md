# CIRCE

An example of how to benefit from a continuous integration workflow hosted at GitHub to control the evolutions of a simple Python project.

Goals are to
- organize code in files, grouped in packages, to comply with main stream Python project structure
- run tests
- use linters and formatters
- manage dependencies

## 1st step. Set-up repo and file structure
- Create project repo @ Git Hub
- Clone it to dev workstation and sync from there or use codespace@github
- Collect an initial   [.gitignore file @ GitHub](https://github.com/github/gitignore/blob/main/Python.gitignore)
- Create folders for sources (`src`), tests (`tests`) and scripts (`scripts`)
- Create at least one package inside `src`

Commit !

## 2nd step. Set-up project metadata
At the root of the project, create a `pyproject.toml` file, to gather standardized (PEP 621) project metadata. Customize the template herebelow:

```
[project]
name = "my-script-project"
version = "0.1.0"
description = "Just a Python script project with tests and tools."
requires-python = ">=3.10"

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
target-version = "py310"

[tool.mypy]
python_version = "3.10"
ignore_missing_imports = true


```
The template mentions 
- `pytest` for testing
- `ruff` for linting 
- `mypy` for type checking.

## 3rd step. Virtual environment for Python
Initiate a virtual environment for Python.

`python3 -m venv .venv`

Then, activate it (adapt the dialect to your OS)

`source .venv/bin/activate`

## 4th step. Introduce code
Populate code. Then only, run:

`pip install -e .[dev]`

This installs the dependencies needed for development.

## 5th step. Test and check
### Populate tests.

`Pytest` requires to use names such as `test_mymodule.py`, import the items to be tested, use simple `assert`s.

To run tests, simply type from the command line:

`pytest`

### lint

To check the sources from the command line:

`ruff check .`

### Scripts
Examples are : 
- a `main.py` script to run the script as a command installed with `pip install -e .`,
- helper scripts to generate test data, clean folders, populate DBs, 
- scripts not meant to be part of the main module or main package.

### CLI tools

For CLI tools to be installed by `pip`, add to `pyproject.toml`.  Then, install with `pip install -e .` to allow the script to run as a command.

```
[project.scripts]
myclitool = "package.source:function"
```

## 6th step. Setup Continuous Integration
Add a protection of the main branch on GitHub requiring all the checks contained in the `ci.yml` workflow to pass to allow a merge.

```

name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install project + dev dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]

    - name: Lint with Ruff
      run: ruff check src/ tests/

    - name: Type check with mypy
      run: mypy src/

    - name: Run tests with pytest
      run: pytest
```