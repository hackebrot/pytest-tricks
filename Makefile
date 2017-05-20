.DEFAULT_GOAL := help

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +


.PHONY: clean-lektor
clean-lektor: ## Remove lektor build artifacts
	@echo "+ $@"
	@lektor clean


.PHONY: clean
clean: clean-pyc ## Remove all file artifacts


.PHONY: install-webpack
install-webpack: ## Install webpack dependencies
	@echo "+ $@"
	@cd webpack && npm install --save-dev webpack babel-core node-sass babel-loader sass-loader css-loader url-loader style-loader file-loader extract-text-webpack-plugin bootstrap bootswatch jquery


.PHONY: build
build: ## Build lektpr site
	@echo "+ $@"
	@lektor build -f webpack


.PHONY: server
server: ## Run local lektor server
	@echo "+ $@"
	@lektor server -f webpack


.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
