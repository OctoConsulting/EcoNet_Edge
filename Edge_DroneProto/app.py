import requests
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy

# from olympe.messages.ardrone3.PilotingSettingsState import Geofence
# from olympe.messages.ardrone3.PilotingState import PositionChanged
# from olympe.messages import gimbal
import argparse
from flask import Flask, jsonify, request
import json
import concurrent.futures
import os 
import time
import math
from time import sleep
import simple_websocket

num_of_drones = 3 
pool = concurrent.futures.ThreadPoolExecutor(max_workers=num_of_drones)

app = Flask(__name__)

def worker(data):

    drone = data['DroneType']
    ip_address = data['DRONE_IP']
    lon = data['LONG']
    lat = data['LAT']

    if drone == 'parrot':

        # send drone to long lat

        # let toto take over
        # ws = simple_websocket.Client(f'ws://toto:5000/toto/{ip_address}')
        # t_end = time.time() + 60 * 2
        # while time.time() < t_end:
        #     data = ws.recive()
        #     loaded = json.loads(data)

        #     x = loaded['x']
        #     y = loaded['y']

        # go home logic

        # tell managmnet that drone came home
        url = 'Manager:5000/api'
        drone = 'parrot_anafi'
        response = requests.post(f'http://{url}/markHome/{drone}')

  
@app.route('/protocal', methods=['POST'])
def managage_commands():
    
    data_loaded = request.json
    
    # submit tasks to the pool
    pool.submit(worker, data_loaded)

    m = {"message": "thread sent to work"}
    
    return jsonify(m)



def test_takeoff(ip):
    DRONE_IP = os.environ.get("DRONE_IP", ip)

    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    
    #assert drone(TakeOff()).wait().success()
    #time.sleep(5)
    print("=======================================================")
    
    

    print("moving to location")
    drone(moveBy(latitude, longitude, altitude).wait())

            
    drone(moveBy(0, 0, 0, math.radians(90))).wait()
    print("rotating")
    drone(moveBy(0, 0, 0, math.radians(-90))).wait()
    time.sleep(5)
    drone.ReturnHomeMinAltitude(50)
    print("returning home")
    assert drone.disconnect()
    
    
if __name__ == "__main__":
    app.run(debug=True)
            

