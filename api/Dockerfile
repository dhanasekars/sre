FROM python:3.11-slim

# Install curl or wget
RUN apt-get update && \
    apt-get install -y curl nano && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./src ./src

# Expose the port the app runs on
EXPOSE 8000