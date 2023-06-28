FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Gunicorn
RUN pip install simple_websocket

# Copy the entire project to the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 8000

# Run the Flask application using Gunicorn
CMD ["python", "Testing.py"]