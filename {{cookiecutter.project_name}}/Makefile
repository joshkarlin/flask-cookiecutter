.DEFAULT_GOAL := init
SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh; conda activate; conda activate

.PHONY: env
env:
	conda env update
	($(CONDA_ACTIVATE) {{cookiecutter.environment_name}} && poetry install)
	@echo "Run 'conda activate {{cookiecutter.environment_name}}' to activate environment"

.PHONY: init
init:
	git init
	pre-commit install
