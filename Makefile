.PHONY: clean-py clean

help:
	@echo "clean-py - remove Python file artifacts"
	@echo "clean - remove all file artifacts"

clean: clean-py

clean-py:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
