import docker
from queue import Queue
from flask import Flask, jsonify, request
import threading

# Constants
DOCKER_IMAGE_BASE_NAME = "drone_image"
EXPOSED_PORT_START = 8000

# Global variables
COORDINATES_QUEUE = Queue()
AVAILABLE_DRONES = []
THREAD_LOCK = threading.Lock()

# Drone profiles
DRONE_PROFILES = {
    "parrot_anafi": {
        "drone_type": "parrot_anafi",
        "ip_address": "192.168.53.1",
        "container_id": None,  # To store the container ID
        "available": True,
        "port": EXPOSED_PORT_START,  # Initial exposed port
    },
    "skydio": {
        "drone_type": "skydio",
        "ip_address": "192.168.53.2",
        "container_id": None,  # To store the container ID
        "available": True,
        "port": EXPOSED_PORT_START + 1,  # Initial exposed port for Skydio
    },
}

# Create a Flask app
app = Flask(__name__)

@app.route("/api/availability", methods=["GET"])
def get_drone_availability():
    return jsonify({"available_drones": AVAILABLE_DRONES})

@app.route("/api/coordinates", methods=["POST"])
def receive_coordinates():
    data = request.get_json()
    longitude = data["longitude"]
    latitude = data["latitude"]
    coordinates = (longitude, latitude)
    COORDINATES_QUEUE.put(coordinates)
    main()
    return jsonify({"message": "Coordinates received and processed"})

def create_and_run_container(drone_profile, coordinates):
    # Retrieve the drone profile information
    getParrot = drone_profile[0]
    # drone_type = drone_profile["drone_type"]
    drone_type = getParrot[0]
    ip_address = drone_profile[1]
    port = drone_profile[4]

    # Create a Docker client
    client = docker.from_env()

    # Build Docker image
    dockerfile = f"""
    FROM python:latest
    COPY droneProtocol.py 
    EXPOSE {port}
    CMD ["python", "droneProtocol.py", "-t", "{drone_type}", "-i", "{ip_address}", "-lon", "{coordinates[0]}", "-lat", "{coordinates[1]}"]
    """
    image_name = f"{DOCKER_IMAGE_BASE_NAME}_{drone_type}_{port}"
    client.images.build(fileobj=dockerfile.encode(), tag=image_name)

    # Create Docker container
    container = client.containers.create(image=image_name, ports={f"{port}/tcp": port})

    # Start the Docker container
    container.start()

    # Store the container ID in the drone profile
    drone_profile["container_id"] = container.id

    # Mark the drone as unavailable and increment the port
    drone_profile["available"] = False
    drone_profile["port"] += 1

def handle_coordinates():
    while not COORDINATES_QUEUE.empty():
        coordinates = COORDINATES_QUEUE.get()
        with THREAD_LOCK:
            if AVAILABLE_DRONES:
                drone_profile = AVAILABLE_DRONES.pop(0)
                threading.Thread(target=create_and_run_container, args=(drone_profile, coordinates)).start()
            else:
                COORDINATES_QUEUE.put(coordinates)
                break

def main():
    handle_coordinates()

def initialize_drones():
    # Initialize the available drones list based on the drone profiles
    for drone_profile in DRONE_PROFILES.values():
        AVAILABLE_DRONES.append(drone_profile["drone_type"])

if __name__ == '__main__':
    # Initialize the drones
    initialize_drones()

    # Run the Flask app
    app.run()
