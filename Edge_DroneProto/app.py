import requests
import olympe
from olympe.messages import *
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
    print("=========================================================")
    print("before int",flush=True)
    drone = data['DroneType']
    ip_address = data['DRONE_IP']
    print(ip_address,flush=True)
    ang = data['ANG'] # x 
    X = data['X']
    #angle = 0 #add models real angle when we get it
    print("=========================================================")
    print("before if",flush=True)
    
    if drone == 'parrot':
        # send drone to long lat
        # let toto take over
        print("=====================================================")
        print("starting movement")
        
        DRONE_IP = os.environ.get("DRONE_IP", ip_address)

        drone = olympe.Drone(DRONE_IP)
        drone.connect()  
                                                                                                                                        #drone.__init__(ip_address)
        #drone(olympe.messages.ardrone3.PilotingSettings.MaxAltitude(current=200,_timeout=20)).wait()
        #time.sleep(5)
        #drone.disconnect()
        #sendDroneOut(ip_address, lat, lon, angle, drone)
        
        
        #assert drone(TakeOff()
                     #>> FlyingStateChanged(state="hovering",_timeout=5)
                     #).wait().success()
        #drone(olympe.messages.ardrone3.PilotingSettings.MaxAltitude(current=100,_timeout=20)).wait()

        #assert drone(moveBy(0,0,-25,0)
                    #>> FlyingStateChanged(state="hovering",_timeout=5)
                    #).wait().success()
        #lat woud be X and Long would be Y, angle is asamith
        #drone(moveBy(75,0,0,0)
                     #>> FlyingStateChanged(state="hovering",_timeout=10)
                     #).wait()
        #drone(FlyingStateChanged(state="flying",_timeout=10))
                     
        #drone(olympe.messages.ardrone3.PilotingSettings.MaxAltitude(current=100,_timeout=20)).wait()
        #assert drone(TakeOff()
                     #>> FlyingStateChanged(state="hovering",_timeout=5)
                     #>> drone(moveBy(0,0,-5,0))
                     #>> FlyingStateChanged(state="hovering",_timeout=1)
                     #>> drone(moveBy(5,0,0,ang))
                     #>> FlyingStateChanged(state="hovering",_timeout=1)
                     #).wait().success()   
        assert drone(

                    TakeOff()

                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> moveBy(0, 0, -25, 0)

                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> moveBy(10, 0, 0, 0)
                    
                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> moveBy(0, 0, 5, 0)
                    
                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> moveBy(0, 0, -5, 0)
                    
                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> moveBy(-10, 0, 0, 0)
                    
                    >> FlyingStateChanged(state="hovering", _timeout=5)

                    >> Landing()

                ).wait().success()
        drone.disconnect()
        #assert behavioral.wait.success()
        ###############################################################################
        ##get cooridnates of the shpt
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
        
        # if the code is broken, it's here, bc we didn't test this code
        #shot_data= {'latitude': newLatitude,
                    #'longitude': newLongitude,
                    #'altitude': newAltitude}
        #json_headers= {'Content-Type': 'application/json'}
        #db_index= requests.post(f'http://localhost:80/db/put_coords',\
                                #data= shot_data,\
                                #headers= json_headers)
        #time.sleep(3)

        #drone(moveBy(0,0,yo,0)
                            #>> FlyingStateChanged(state="flying",_timeout=10)
                            #).wait()
        #time.sleep(yo/2)
        ###############################################################################
        #set gimbal to a default angl e of 30 degrees to see the target
        #drone(olympe.messages.gimbal.set_target(
            #gimbal_id=0,
            #control_mode="position",
            #yaw_frame_of_reference="none",
            #yaw=0.0,
            #pitch_frame_of_reference="absolute",
            #pitch=-45.0, #pre set to get the inital detection
            #roll_frame_of_reference="none",
            #roll=10.0,)).wait()
        
        #time.sleep(3)
        
        #drone(olympe.messages.follow_me.start(1)).wait()
        
        
        #########################################################################
        #
        #start_time = time.time()
        #ws = simple_websocket.Client(f'ws://toto:5000/toto/{ip_address}')
        #ws = simple_websocket.Client(f'ws://toto:5000/toto/{ip_address}')
        #drone(olympe.messages.follow_me.start(1)).wait()

        #current_time = time.time()
        #elapsed_time = current_time - start_time
        #data = ws.recive()
        #loaded = json.loads(data)
        #pitch = x 
        #roll = y
        #TODO implement the camera update using Toto
        #Idea: create some if statements to monitor where in the screen x and y are since pitch and roll are -90 -> 90 noninclusive and spherical 
        #x = loaded['x']
        #y = loaded['y']
        #print(x, flush=True)
        #print(y, flush=True)
        #print("before close")
        
            #if elapsed_time >= 10:
        #time.sleep(60)
        #assert drone(moveBy(-X,0,0,-ang)
                        #>> FlyingStateChanged(state="hovering",_timeout=5)
                        #).wait().success()
        ###############################################################
        #reset the gimbal
        #drone(olympe.messages.gimbal.reset_orientation(gimbal_id=0)).wait()
        #time.sleep(1)
        ###############################################################
        #land the drone
        #assert drone(Landing()).wait().success()
        
                #break
        print("close complete")

        #ws.close()
            
        ########################################################################
        #return home
        assert drone(moveBy(0,0,-15,0)
                            >> FlyingStateChanged(state="hovering",_timeout=1)
                            ).wait().success()
        assert drone(moveBy(-70,0,0,-ang)
                     >> FlyingStateChanged(state="hovering",_timeout=1)
                     ).wait().success()
        ######################################################################
        #reset the gimbal
        drone(olympe.messages.gimbal.reset_orientation(gimbal_id=0)).wait()
        time.sleep(1)
        ######################################################################
        #land the drone
        assert drone(Landing()).wait().success()
        
        #######################################################################
        #return the battery percentage of the drone after flight
        batteryPercent = drone.get_state(olympe.messages.common.CommonState.BatteryStateChanged)["percent"]
        print("Battery percentage: ", batteryPercent)
        #TODO send the battery percentage after the flight to surge
        drone.disconnect()

        #########################################################################
        #disconnect the drone
        
        #tell managmnet that drone came home
        url = 'Manager:5000/api'
        drone = 'parrot_anafi'
        response = requests.post(f'http://{url}/markHome/{drone}')

class flyingStatus(Enum):
    TAKE_OFF = 0
    IN_PROGRESS = 1
    ARRIVED_TO_SHOT = 2
    RETURNING = 3
    RETURNED = 4
    
    
  
@app.route('/protocal', methods=['POST'])
def managage_commands():
    
    data_loaded = request.json
    
    # submit tasks to the pool
    pool.submit(worker, data_loaded)

    m = {"message": "thread sent to work"}
    
    return jsonify(m)

def returnToHome(ip, latitude, longitude, angle, droneF):
    
    drone = droneF
    drone.ReturnHomeMinAltitude(50)
    print("returning home")
    assert drone(moveBy(-latitude,-longitude,0,-angle)
                 >> FlyingStateChanged(state="hovering",_timeout=5)
                 ).wait().success()
    print("Drone returned")

    drone(olympe.messages.gimbal.reset_orientation(gimbal_id=0)).wait()
    time.sleep(1)
    assert drone(Landing()).wait().success()
    
    #return the battery percentage of the drone after flight
    batteryPercent = drone.get_state(olympe.messages.common.CommonState.BatteryStateChanged)["percent"]
    print("Battery percentage: ", batteryPercent)

    #send the battery percentage out
    drone.disconnect()

...

def testGimbalWithToTo(ip, droneF):
    drone = droneF
    
    drone(olympe.messages.gimbal.reset_orientation(gimbal_id=0)).wait()
    time.sleep(5)
    drone(olympe.messages.gimbal.set_target(
        gimbal_id=0,
        control_mode="position",
        yaw_frame_of_reference="none",
        yaw=10.0,
        pitch_frame_of_reference="absolute",
        pitch=-15.0,
        roll_frame_of_reference="none",
        roll=10.0,)).wait()
    
    print("=========== done moving=============== ")
    start_time = time.time() + 5
    current_time = time.time()
    elapsed_time = current_time - start_time
    flyingStatus.ARRIVED_TO_SHOT = 4
                
            

        

def sendDroneOut(ip, latitude, longitude, angle, droneF):
    
    drone = droneF 
    assert drone(TakeOff()
                 >> FlyingStateChanged(state="hovering",_timeout=5)
                 ).wait().success()
    
    #drone(olympe.messages.ardrone3.PilotingSettings.MaxAltitude(current=100,_timeout=20)).wait()
    
    assert drone(moveBy(0,0,2,0)
                 >> FlyingStateChanged(state="hovering",_timeout=5)
                 ).wait().success()
    
    assert drone(moveBy(latitude,longitude,0,angle)
                 >> FlyingStateChanged(state="hovering",_timeout=5)
                 ).wait().success()

    drone(olympe.messages.gimbal.set_target(
        gimbal_id=0,
        control_mode="position",
        yaw_frame_of_reference="none",
        yaw=10.0,
        pitch_frame_of_reference="absolute",
        pitch=-30.0,
        roll_frame_of_reference="none",
        roll=10.0,)).wait()
    time.sleep(3)
    
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

    
if __name__ == "__main__":
    app.run(debug=True)
            

