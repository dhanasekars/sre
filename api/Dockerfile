FROM ubuntu:latest
LABEL authors="dhanasekarsubramaniam"

# Use the official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and DML alembic
COPY ./src ./src
COPY ./alembic /app/alembic
COPY alembic.ini alembic.ini

# Expose the port the app runs on
EXPOSE 8000

# Command to run Alembic migrations and then start the application
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
