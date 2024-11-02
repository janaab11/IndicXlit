# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install g++ and other build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the rest of your application code to the container
COPY . .

# Install dependencies
RUN python -m pip install --upgrade "pip<24.1"
RUN pip install -e .

# Expose the port the app runs on
EXPOSE 8888

# Define environment variable to prevent Python from buffering stdout/stderr
# and writing byte code to file
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Run the server with uWSGI, binding to all interfaces on the PORT environment variable
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
