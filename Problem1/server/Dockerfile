# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
