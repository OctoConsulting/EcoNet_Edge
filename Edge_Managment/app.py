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
    longitude = data["longitude"]
    latitude = data["latitude"]
    angle =  data['Angle']
    x = data['Distance']  
    #data['Weapon'] = "pistol"
    #data['Azimuth'] = "225" # angle of gun being shot 
    coordinates = (x, angle)

    # searching for avalible drine
    for drone_profile in DRONE_PROFILES.values():
        if drone_profile["available"]:
            drone_profile["available"] = False
            print(drone_profile["drone_type"])
            m = launch(longitude, latitude, drone_profile)
            return m
    
    # if there are no avalible drones
    COORDINATES_QUEUE.put(coordinates)
    
    return jsonify({"message": "no drones avalible"})

def launch(angle, x, drone_profile):

        DTYPE = drone_profile["drone_type"]
        DADDR = drone_profile["ip_address"]
        
        params = {
            "DroneType": DTYPE,
            "DRONE_IP": DADDR,
            "ANG": angle,
            "X": x,
        }

        url = 'http://proto1:5000/protocal'
        response = requests.post(url, json=params)

        return str(response)


if __name__ == '__main__':
    app.run(debug=True)
