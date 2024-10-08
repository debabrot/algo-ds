# Define variables
VENV_DIR = .algo_venv
BUILD_DIR = build
CACHE_DIR = __pycache__
PYTEST_CACHE_DIR = .pytest_cache
EGG_INFO_DIR = algo_ds.egg-info

venv:
	python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

install:
	pip install -r requirements.txt

build:
	python3 setup.py develop
	@echo "Algo module build completed"
	pip install -e .

lint:
	@pylint --disable=R,C $(shell find . -name "*.py")

test:
	pytest

clean:
	rm -rf $(VENV_DIR)
	@echo "Virtual environment deleted"
	rm -rf $(BUILD_DIR)
	@echo "Build directory deleted"
	rm -rf $(CACHE_DIR)
	@echo "Cache directory deleted"
	rm -rf $(PYTEST_CACHE_DIR)
	@echo "Pytest Cache directory deleted"
	rm -rf $(EGG_INFO_DIR)
	@echo "Egg info directory deleted"
