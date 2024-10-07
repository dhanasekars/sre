FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and DML alembic
COPY ./src ./src
COPY ./alembic ./alembic
COPY ./alembic.ini .

# Expose the port the app runs on
EXPOSE 8000
