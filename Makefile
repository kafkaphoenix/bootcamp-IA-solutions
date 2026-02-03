.DEFAULT_GOAL := help

# AutoDoc
# -------------------------------------------------------------------------
.PHONY: help
help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

.PHONY: run-local-mlflow
run-local-mlflow: ## Run local MLflow server
	uv run mlflow server --host 127.0.0.1 --port 8080

.PHONY: run-project
run-project: ## Run project
	uv run python -m retrieval.main

.PHONY: start-movie-recommender
start-movie-recommender: ## Start movie recommender app
	make run-local-mlflow & make run-project