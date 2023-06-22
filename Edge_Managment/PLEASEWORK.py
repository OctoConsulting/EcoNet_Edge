import docker

# Define the necessary variables
port = 8000
drone_type = "quadcopter"
ip_address = "192.168.1.100"
coordinates = [34.0522, -118.2437]
DOCKER_IMAGE_BASE_NAME = "my_docker_image"

# Create a Docker client
client = docker.from_env()

# Build Docker image
dockerfile = f"""
FROM python:latest
RUN pip install requests
COPY droneProtocol.py /
EXPOSE 8000
CMD ["python", "droneProtocol.py", "-t", "{drone_type}", "-i", "{ip_address}", "-lon", "{coordinates[0]}", "-lat", "{coordinates[1]}"]
"""
image_name = f"{DOCKER_IMAGE_BASE_NAME}_{drone_type}_{port}"
client.images.build(fileobj=dockerfile.encode(), tag=image_name)

# Create Docker container
container = client.containers.create(image=image_name, ports={f"{port}/tcp": port})

# Start the Docker container
container.start()

# Store the container ID in the drone profile
drone_profile = {
    "container_id": container.id,
    "available": False,
    "port": port
}

# Mark the drone as unavailable and increment the port
drone_profile["available"] = False
drone_profile["port"] += 1

# Additional operations with the running container or drone profile can be performed here
# ...

# Stop and remove the container when done
container.stop()
container.remove()
