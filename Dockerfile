# Dockerfile
FROM python:3.8

# Copy your application code
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Your application start command
CMD ["python", "app.py"]
