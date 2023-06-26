from queue import Queue
from flask import Flask, jsonify, request
import threading
import requests
import simple_websocket
import json
import time
# Constants
DOCKER_IMAGE_BASE_NAME = "drone_image"
EXPOSED_PORT_START = 8005
time.sleep(5)
# Global variables
COORDINATES_QUEUE = Queue()
AVAILABLE_DRONES = []
Unavailable = []
THREAD_LOCK = threading.Lock()
wc = simple_websocket.Client('ws://proto1:5000/protocal')

# Drone profiles
DRONE_PROFILES = {
    "parrot_anafi": {
        "drone_type": "parrot",
        "ip_address": "192.168.53.1",
        "available": True,
    },
    "skydio": {
        "drone_type": "skydio",
        "ip_address": "192.168.53.2",
        "available": True,
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
    for drone_profile in DRONE_PROFILES.values():
        if drone_profile["available"]:
            drone_profile["available"] = False
            print(drone_profile["drone_type"])
            m = launch(longitude, latitude, drone_profile)
            return m
        else:
            return jsonify({"message": "drone"})
    #m = launch(latitude, longitude)
    #m = launch(longitude, latitude)
    #m = launch(1, 1, 1)
    #send_command_to_container()
    #return m

def launch(x, y, z):

        if z:
            #z["available"] = False
            DTYPE = z["drone_type"]
            DADDR = z["ip_address"]
            
            params = {
                "DroneType": DTYPE,
                "DRONE_IP": DADDR,
                "LONG": x,
                "LAT": y,
                "source": "launch"
            }
            print(params)
            # response = requests.get(flask_url, json=params
            wc.send(json.dumps(params))

            return wc.receive()
            #return params

        else:
            COORDINATES_QUEUE.put(coordinates)





def initialize_drones():
    # Initialize the available drones list based on the drone profiles
    for drone_profile in DRONE_PROFILES.values():
        AVAILABLE_DRONES.append(drone_profile)

if __name__ == '__main__':
    # Initialize the drones
    initialize_drones()
    # Run the Flask app
    
    app.run(debug=True)
