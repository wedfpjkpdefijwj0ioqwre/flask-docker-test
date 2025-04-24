# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]

