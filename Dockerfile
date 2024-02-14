# Use the official Python base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install Firefox browser and driver
RUN apt-get update && apt-get install -y firefox-esr

# Copy the local code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Entry point - run your script
CMD ["python", "main.py"]
