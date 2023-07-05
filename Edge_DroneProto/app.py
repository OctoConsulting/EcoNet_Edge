import requests
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy
from olympe.messages.gimbal import *
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from olympe.enums.ardrone3.PilotingState import FlyingStateChanged_State as FlyingState
#from olympe.messages.ardrone3.GPSSettingState import GPSFixStateChanged
# from olympe.messages.ardrone3.PilotingState import PositionChanged

import argparse
from flask import Flask, jsonify, request
import json
import concurrent.futures
import os 
import time
import math
from enum import Enum
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
    angle = 0 #add models real angle when we get it

    if drone == 'parrot':
        # send drone to long lat
        #sendDroneOut(ip_address, lat, lon, angle)
        # let toto take over
        testGimbalWithToTo(ip_address)
        if(flyingStatus.ARRIVED_TO_SHOT == 4):
            ws = simple_websocket.Client(f'ws://toto:5000/toto/{ip_address}')
            t_end = time.time() + 60 * 2
            while time.time() < t_end:
                data = ws.recive()
                loaded = json.loads(data)
                x = loaded['x']
                y = loaded['y']
        else:
            flyingStatus.ARRIVED_TO_SHOT = 2
        
        # go home logic
        returnToHome(ip_address, lat, lon, angle)
        # tell managmnet that drone came home
        url = 'Manager:5000/api'
        drone = 'parrot_anafi'
        response = requests.post(f'http://{url}/markHome/{drone}')

class flyingStatus(Enum):
    TAKE_OFF = 0
    IN_PROGRESS = 1
    ARRIVED_TO_SHOT = 2
    RETURNED = 3
    
    
  
@app.route('/protocal', methods=['POST'])
def managage_commands():
    
    data_loaded = request.json
    
    # submit tasks to the pool
    pool.submit(worker, data_loaded)

    m = {"message": "thread sent to work"}
    
    return jsonify(m)

def returnToHome(ip, latitude, longitude, angle):
    with olympe.Drone(ip) as drone:
        drone.ReturnHomeMinAltitude(50)
        print("returning home")

        drone(moveBy(latitude,longitude,0,-angle)).wait()

        print("Drone returned")

        drone(olympe.messages.gimbal.reset_orientation(gimbal_id=0)).wait()
        assert drone(Landing()).wait().success()
        #return the battery percentage of the drone after flight
        batteryPercent = drone.get_state(olympe.messages.common.CommonState.BatteryStateChanged)["percent"]
        print("Battery percentage: ", batteryPercent)

        #send the battery percentage out
        assert drone.disconnect()

    ...

def testGimbalWithToTo(ip):
    with olympe.Drone(ip) as drone:
        drone.__init__(ip)
        drone.connect()   
        drone(olympe.messages.gimbal.set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=10.0,
            pitch_frame_of_reference="absolute",
            pitch=-45.0,
            roll_frame_of_reference="none",
            roll=10.0,)).wait()
        
        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= 5:
                flyingStatus.ARRIVED_TO_SHOT = 4
                break

        

def sendDroneOut(ip, latitude, longitude, angle):
    with olympe.Drone(ip) as drone:
        
        drone.__init__(ip)
        drone.connect()   
        assert drone(TakeOff()).wait().success()
        drone(olympe.messages.ardrone3.PilotingSettings.MaxAltitude(current=100,_timeout=20))
        drone(moveBy(0,0,50,0)).wait()
        drone(moveBy(latitude,longitude,0,angle)).wait()
        

        flying_states = FlyingState._bitfield_type_("takingoff|hovering|flying")

        if drone.get_state(olympe.messages.ardrone3.PilotingState.FLyingStateChanged)["hovering"] in flying_states:
            assert True, "The drone is hovering"
            flyingStatus.ARRIVED_TO_SHOT = 4
        else:
            flyingStatus.IN_PROGRESS

        drone(olympe.messages.gimbal.set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",
            yaw=10.0,
            pitch_frame_of_reference="absolute",
            pitch=-45.0,
            roll_frame_of_reference="none",
            roll=10.0,)).wait()
        
        task_1 = drone(olympe.messages.ardrone3.GPSSettingsState.GPSFixStateChanged(_policy='wait'))
        print(task_1.explain())
        gps_location = drone.get_state(olympe.messages.ardrone3.PilotingState.GpsLocationChanged)

        newLatitude = gps_location['latitude']
        newLongitude = gps_location['longitude']
        newAltitude = gps_location['altitude']


        print("=======================================================")
        print("Shot Lat: {}".format(newLatitude))
        print("Shot Long: {}".format(newLongitude))
        print("Shot Altitude: {}".format(newAltitude))
        print("=======================================================")


        #TODO send lat, long, and altitude with requests

    ...


def test_takeoff(ip):
    DRONE_IP = os.environ.get("DRONE_IP", ip)

    with olympe.Drone(DRONE_IP) as drone:
        
        drone.__init__(DRONE_IP)
        drone.connect()   
        assert drone(TakeOff()).wait().success()
        
        print("=======================================================")

        task_1 = drone(olympe.messages.ardrone3.GPSSettingsState.GPSFixStateChanged(_policy='wait'))
        print(task_1.explain())

        gps_location = drone.get_state(olympe.messages.ardrone3.PilotingState.GpsLocationChanged)
        latitude = gps_location['latitude']
        longitude = gps_location['longitude']
        altitude = gps_location['altitude']

        print("Lat: {}".format(latitude))
        print("Long: {}".format(longitude))
        print("Altitude: {}".format(altitude))


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
            

