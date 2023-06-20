FROM python:3.9

# Set the working directory inside the container
WORKDIR /drones



RUN ["python", "droneProtocol.py"]


# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]