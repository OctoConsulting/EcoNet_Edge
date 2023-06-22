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
        "container_name": "containerA",
        "available": True,
        "port": EXPOSED_PORT_START,  # Initial exposed port
    },
    "skydio": {
        "drone_type": "skydio",
        "ip_address": "192.168.53.2",
        "container_name": "containerB",
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

def send_command_to_container(container_name, command):
    # Connect to the Docker daemon using the Docker SDK
    client = docker.from_env()

    try:
        # Find the container with the specified name
        container = client.containers.get(container_name)

        # Execute a command inside the container
        response = container.exec_run(command)

        # Check Flask script response code
        if response.exit_code == 200:
            for drone_profile in AVAILABLE_DRONES:
                if drone_profile["container_name"] == container_name:
                    drone_profile["available"] = False

        # Print the command output
        print(response.output.decode().strip())
    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")

def create_and_run_container(drone_profile, command):
    # Retrieve the drone profile information
    container_name = drone_profile["container_name"]

    # Send command to the container
    send_command_to_container(container_name=container_name, command=command)

def handle_coordinates():
    while not COORDINATES_QUEUE.empty():
        coordinates = COORDINATES_QUEUE.get()
        with THREAD_LOCK:
            if AVAILABLE_DRONES:
                drone_profile = AVAILABLE_DRONES.pop(0)
                command = ["echo", "Hello"]
                threading.Thread(target=create_and_run_container, args=(drone_profile, command)).start()
            else:
                COORDINATES_QUEUE.put(coordinates)
                break

def main():
    handle_coordinates()

def initialize_drones():
    # Initialize the available drones list based on the drone profiles
    for drone_profile in DRONE_PROFILES.values():
        AVAILABLE_DRONES.append(drone_profile)

if __name__ == '__main__':
    # Initialize the drones
    initialize_drones()

    # Run the Flask app
    app.run()
