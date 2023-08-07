# Use a base image suitable for your application (e.g., python:3.9)
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy your application files to the container
COPY app.py requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which your Flask app runs
EXPOSE 5000

# Set the entrypoint command to run your Flask app
CMD ["python", "app.py"]
