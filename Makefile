INTERPRETER := python
TESTS_DIR := tests
PKG_SOURCE := med_crawler

.DEFAULT_GOAL := run

format:
	black $(PKG_SOURCE) $(TEST_DIR)
.PHONY: format

types:
	mypy $(PKG_SOURCE) $(TEST_DIR)
.PHONY: types

test: types
	pytest $(TESTS_DIR)
.PHONY: test

cov: types
	pytest $(TESTS_DIR) --cov $(PKG_SOURCE) --cov-report=term-missing
.PHONY: cov

setup:
	$(INTERPRETER) -m pip install --upgrade pip
.PHONY: setup

install: setup
	$(INTERPRETER) -m pip install -e ".[dev]"
.PHONY: install
