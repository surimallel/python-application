# Python application build demo

A small Python package that demonstrates a typical build in Jenkins: create an
isolated environment, install the project and its test tools, run unit tests,
and build distributable Python packages.

## Application

The `hello-jenkins` command prints a greeting:

```text
$ hello-jenkins --name Ada
Hello, Ada!
```

## Run locally

Python 3.9 or newer is required. From the repository root:

```bash
python -m venv .venv
# PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m pytest
python -m build
```

The build produces a wheel and source archive in `dist/`.

## Run in Jenkins

The included `Jenkinsfile` uses a Linux Jenkins agent with Python 3 available
as `python3`. Create a Pipeline job pointing at this repository (or configure
the repository's multibranch pipeline); Jenkins will discover the `Jenkinsfile`
and run the build stages. The pipeline publishes JUnit test results and
archives the generated packages as build artifacts.

The pipeline uses the standard Jenkins Pipeline and JUnit functionality. No
Python-specific Jenkins plugin is needed.
