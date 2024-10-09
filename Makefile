# Makefile

.PHONY: help create-env build-api-image run-docker-compose setup

# Default target, will show help
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

create-env: ## Create the .env file and prompt for user input
	@echo "Creating .env file..."
	@touch .env
	@echo "ENVIRONMENT=local" > .env
	@read -p "Enter DATABASE_USER: " user; echo "DATABASE_USER=$$user" >> .env
	@read -p "Enter DATABASE_PASSWORD: " password; echo "DATABASE_PASSWORD=$$password" >> .env
	@read -p "Enter DATABASE_LOCAL_HOST (default: localhost:3306): " host; echo "DATABASE_LOCAL_HOST=$${host:-localhost:3306}" >> .env
	@read -p "Enter DATABASE_NAME: " dbname; echo "DATABASE_NAME=$$dbname" >> .env
	@read -p "Enter DATABASE_ROOT_USER_PWD: " root_pwd; echo "DATABASE_ROOT_USER_PWD=$$root_pwd" >> .env
	@echo ".env file created successfully."

build-api-image: ## Build the Docker image for the API (using api/Dockerfile)
	@echo "Building API Dockerfile..."
	@docker build -t fastapi-app1 ./api

run-docker-compose: ## Run docker-compose to bring up services
	@echo "Running docker-compose..."
	@docker-compose up -d

setup: create-env build-api-image run-docker-compose ## Full setup: create .env, build Dockerfile, run docker-compose
	@echo "Setup complete."


MSG ?= Daily checkin

format:
	#format code
	black .

lint:
	#flake8 or #pylint
	@pylint -j 4 --rcfile=pylint.rc api/src/

git:
	#git push
	@git add .
	@git commit -m "$(MSG)"
	@git push

startapp:
	python -m api.src.main

dcup:
	docker-compose up --build
