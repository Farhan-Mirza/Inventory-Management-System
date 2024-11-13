# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any necessary dependencies (if you have any)
# For this example, there are no external dependencies
# If you have a requirements.txt, you can uncomment the next line
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]