FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and DML alembic
COPY ./src ./src
COPY ./alembic /app/alembic
COPY alembic.ini alembic.ini
#COPY wait-for-it.sh .

# Expose the port the app runs on
EXPOSE 8000

# Command to run Alembic migrations and then start the application
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
#CMD ["./wait-for-it.sh", "db:3306", "--", "sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload"]
