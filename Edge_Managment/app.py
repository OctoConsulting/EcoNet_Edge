from queue import Queue
from flask import Flask, jsonify, request
import threading
import requests
import simple_websocket
import json
import time
# Global variables
COORDINATES_QUEUE = Queue()

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

@app.route("/api/markHome/<profile>", methods=["POST"])
def mark_drone_home(profile):
    DRONE_PROFILES[profile]['available'] = True
    print('home!', flush=True)

    return jsonify({profile: DRONE_PROFILES[profile]})

@app.route("/api/coordinates", methods=["POST"])
def receive_coordinates():
    data = request.get_json()
    global longitute
    longitude = data["longitude"]
    global latitude
    latitude = data["latitude"]
    coordinates = (longitude, latitude)
    COORDINATES_QUEUE.put(coordinates)

    # searching for avalible drine
    print(DRONE_PROFILES, flush=True)
    for drone_profile in DRONE_PROFILES.values():
        print(drone_profile, flush=True)
        print(drone_profile["available"], flush=True)
        
        if drone_profile["available"]:
            drone_profile["available"] = False
            print(drone_profile["drone_type"])
            m = launch(longitude, latitude, drone_profile)
            return m
    
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
            url = 'http://proto1:5000/protocal'
            response = requests.post(url, json=params)

            return str(response.json)

        else:
            COORDINATES_QUEUE.put(coordinates)

if __name__ == '__main__':
    app.run(debug=True)
