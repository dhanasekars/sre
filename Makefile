# Variables
ENV_FILE = .envnew

# Default target
.PHONY: all
all: create_env install_db

# Prompt for user input and create .env file
.PHONY: create_env
create_env:
	@echo "Creating .env file. Please enter the following details:"
	@read -p "Database User: " DATABASE_USER; \
	read -s -p "Database Password: " DATABASE_PASSWORD; echo; \
	read -p "Database Name: " DATABASE_NAME; \
	read -s -p "MariaDB Root User Password: " MARIADB_ROOT_USER_PWD; echo; \
	echo "ENVIRONMENT=local" > $(ENV_FILE); \
	echo "DATABASE_USER=$$DATABASE_USER" >> $(ENV_FILE); \
	echo "DATABASE_PASSWORD=$$DATABASE_PASSWORD" >> $(ENV_FILE); \
	echo "DATABASE_LOCAL_HOST=localhost:3306" >> $(ENV_FILE); \
	echo "DATABASE_NAME=$$DATABASE_NAME" >> $(ENV_FILE); \
	echo "DATABASE_ROOT_USER_PWD=$$MARIADB_ROOT_USER_PWD" >> $(ENV_FILE); \
	echo ".env file created successfully."

# Commands
MYSQL = mysql
MYSQL_CMD = $(MYSQL) -u root -p$$MARIADB_ROOT_USER_PWD
MYSQL_DB_CMD = $(MYSQL_CMD) -e
MYSQL_SETUP = $(MYSQL_CMD) -e "CREATE DATABASE IF NOT EXISTS $(DATABASE_NAME); \
                                 CREATE USER IF NOT EXISTS '$(DATABASE_USER)'@'localhost' IDENTIFIED BY '$(DATABASE_PASSWORD)'; \
                                 GRANT ALL PRIVILEGES ON $(DATABASE_NAME).* TO '$(DATABASE_USER)'@'localhost'; \
                                 FLUSH PRIVILEGES;"

# Install MariaDB (if not installed) and set up the database
.PHONY: install_db
install_db:
	@echo "Checking for package manager..."
	@if command -v brew &> /dev/null; then \
		echo "Installing MariaDB using brew..."; \
		brew install mariadb; \
		brew services start mariadb; \
	elif command -v apt &> /dev/null; then \
		echo "Installing MariaDB using apt..."; \
		sudo apt update && sudo apt install -y mariadb-server; \
		sudo systemctl start mariadb; \
		sudo systemctl enable mariadb; \
	else \
		echo "No compatible package manager found (apt or brew). Please install MariaDB manually."; \
		exit 1; \
	fi
	sleep 5
	@echo "Setting up the database..."
	$(MYSQL_SETUP)
	@echo "Database setup complete."

# Stop MariaDB service
.PHONY: stop_db
stop_db:
	@echo "Stopping MariaDB..."
	@if command -v systemctl &> /dev/null; then \
		sudo systemctl stop mariadb; \
	else \
		brew services stop mariadb || echo "MariaDB not running"; \
	fi

# Clean up database (drop database and user)
.PHONY: clean_db
clean_db:
	@echo "Cleaning up the database..."
	$(MYSQL_CMD) -e "DROP USER IF EXISTS '$(DATABASE_USER)'@'localhost';"
	$(MYSQL_CMD) -e "DROP DATABASE IF EXISTS $(DATABASE_NAME);"
	@echo "Database cleanup complete."

# Help command to show available targets
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  make create_env - Prompt for user input and create .env file"
	@echo "  make install_db - Install and set up the MariaDB database"
	@echo "  make stop_db    - Stop the MariaDB service"
	@echo "  make clean_db   - Drop the database and user"
	@echo "  make help       - Show this help message"

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
