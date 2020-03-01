# {{cookiecutter.project_name}}

This project is a Flask app with an API made using FastAPI and with asynchronous task execution using rq. Redis is used as the messaging queue.

{{cookiecutter.project_description}}

## Requirements

- Conda https://docs.conda.io/en/latest/miniconda.html
- Poetry https://github.com/python-poetry/poetry

## Setup repo

1. Install requirements listed above
1. Disable poetry virtual env to install poetry packages into conda environment
  `poetry config virtualenvs.create false`
  (add the `--local` flag if you want to only apply the config change to this repo)
1. Create the environment
  `make env`
1. Activate the environment
  `conda activate {{cookiecutter.environment_name}}`
1. Initialise repo - creates a .git directory and sets up pre-commit hooks
  `make init`

The specific `make` commands being run are defined in `Makefile`.

