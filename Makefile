.PHONY: clean-py clean

help:
	@echo "clean-py - remove Python file artifacts"
	@echo "clean - remove all file artifacts"
	@echo "server - run a local lektor server"

clean: clean-py

clean-py:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

server:
	lektor server -f webpack
