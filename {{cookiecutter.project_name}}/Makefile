.DEFAULT_GOAL := init

.PHONY: env
env:
	conda env create
	poetry install
	echo "Run conda activate {{cookiecutter.environment_name}} to activate environment"

.PHONY: init
init:
	git init
	pre-commit install
