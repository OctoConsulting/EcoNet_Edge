from queue import Queue
from flask import Flask, jsonify, request
import threading
import requests
import simple_websocket
import json

# Constants
DOCKER_IMAGE_BASE_NAME = "drone_image"
EXPOSED_PORT_START = 8005

# Global variables
COORDINATES_QUEUE = Queue()
AVAILABLE_DRONES = []
THREAD_LOCK = threading.Lock()
wc = simple_websocket.Client('ws://protocal:5000/protocal')

# Drone profiles
DRONE_PROFILES = {
    "parrot_anafi": {
        "drone_type": "parrot",
        "ip_address": "192.168.53.1",
        "container_name": "proto1",
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
    global longitute
    longitude = data["longitude"]
    global latitude
    latitude = data["latitude"]
    coordinates = (longitude, latitude)
    COORDINATES_QUEUE.put(coordinates)
    
    #main()
    m = launch(1, 1, 1)
    #send_command_to_container()
    return m

def launch(DTYPE,DADDR,DNAME):

    # Connect to the Docker daemon using the Docker SDK
    #client = docker.from_env()
    CONTAINER_NAME = "HELLO" ## SHOULD BE AVAILABLE DRONE
    #DNAME = DNAME
    # flask_url = "http://proto1:5000/api/command"

    DroneTak = "hello"
    DRONE_IP = "IP"

    params = {
        "DroneType": "parrot",
        "DRONE_IP": "hello",
        "LONG": "223.2",
        "LAT": "2232"
    }
    # response = requests.get(flask_url, json=params
    wc.send(json.dumps(params))

    return wc.receive()

def handle_coordinates():
    while not COORDINATES_QUEUE.empty():
        coordinates = COORDINATES_QUEUE.get()
        with THREAD_LOCK:
            if AVAILABLE_DRONES:
                drone_profile1 = AVAILABLE_DRONES.pop(0)
                
                DTYPE = drone_profile1["drone_type"]
                DADDR = drone_profile1["ip_address"]
                DNAME = drone_profile1["container_name"]
             

                threading.Thread(target=launch, args=(DTYPE, DADDR, DNAME)).start()
                
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
    
    app.run(debug=True)
