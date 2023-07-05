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
from flask_sock import Sock
from time import sleep

num_of_drones = 3 
pool = concurrent.futures.ThreadPoolExecutor(max_workers=num_of_drones)

app = Flask(__name__)
sock = Sock(app)

def worker(data):
    #here parse the commands and fitures of what our functiioons to run to send infor to the drone
    #test_takeoff()
    ip_address = "192.168.53.1"
    #test_takeoff(ip_address)

    if data['source'] == 'launch':
        test_takeoff(ip_address)

        target = data['DroneType']
        ip_address = data['Drone_IP']
        lon = data['LONG']
        lat = data['LAT']
        #test_takeoff()
        if target == "parrot":
  

                test_takeoff(ip_address)
                #ONCE AT  1 , 1 , 1
                #CONNECT TO WEBSOCKET
                #START WHILE LOOP (BELOW)

                #from toto
                #params = {
                    #"Point_of_interest": {
                        #'x': 2, 
                        #'y': 4
                    #},
                #}

                #activate totcv
                #t_end = time.time() + 60 * 2
                #while time.time() < t_end:
                    #websoket
                    #data.revice()
                    #move drone point to the point that is givven in data
                
                    #if data.receive == return
                        #send home
                #send home

                
                #the moveTo command send the drone to a certain coordinate point at a certain height
                #dummy values for now but this is the frame

                #1: inital long lat
                #2: once at long lat --> eavlute totocv
                    #get feedback and commit movments
                    
                #3: go back home logic

                    #drone.disconnect()
                #  http request to some endpoint in managmnt stating that this done has come back home
             
                # IF OBJECT NOT FOUND IN 30 SECOND
                #     THEN RETURN TO CORDINATE XYZ
                    #  ALSO SEND CURL COMMAND TO CONTAINER:5000 
                        # IN MESSAGE TO CONTAINER SEND ID Value
        
        elif target == "skydio":
            #Skydio drone code here
            pass

  


@sock.route('/protocal', methods=['GET'])
def managage_commands(ws):
    
    try:
        
        while True:
 
            data = ws.receive()
            
            data_loaded = json.loads(data)
            
            print(data_loaded)

            # submit tasks to the pool
            pool.submit(worker, data_loaded)
            m = {"message": "thread sent to work"}
            ws.send(json.dumps(data_loaded))
            
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        pass

    return jsonify({"message": "connection closed"})

def test_takeoff(ip):
    DRONE_IP = os.environ.get("DRONE_IP", ip)

    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    
    assert drone(TakeOff()).wait().success()
    time.sleep(5)
    assert drone(Landing()).wait().success()
    gps_info = olympe.messages.controller_info.gps()
    print("GPS info: ", gps_info)
    drone.disconnect

def parrot_intake():
    sleep(10)
    return 

def skydio_intake():
    sleep(1)
    return

# def main(args):
#     target = args.target
#     ip_address = args.ip_address
#     physical_port = args.physical_port
#     lon = args.lon
#     lat = args.lat

 

#     if target == "skydio":
#         with Olympe() as drone:
#             drone.connect(ip_address)
#             # Skydio drone code here

 

#     elif target == "parrot":
#         with Olympe() as drone:
#             drone.connect()
#             latitude = lat
#             longitude = lon
#             altitude = 20
#             geofence_size = 0.01
#             drone.start()

#             #the moveTo command send the drone to a certain coordinate point at a certain height
#             #dummy values for now but this is the frame
#             drone.disconnect()

#     else:
#         print("Drone type not supported")

    
DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
def test_find():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    drone.start()
    altitude = 50

# #     drone(TakeOff()).wait()

    # Calibrate the magnetometer 
    #temporary fix
    assert drone(MagnetoCalibration(1)).wait()

    def gps_update_callback(event):
        print("GPS update state changed:", event.args["state"])
    

    # Register the callback for GPS update state changes
    assert drone.subscribe(GPSUpdateStateChanged(gps_update_callback))

    latitude = drone.get_state(PositionChanged)["latitude"]
    longitude = drone.get_state(PositionChanged)["longitude"]

    assert drone(set_home=[latitude,longitude,altitude]).wait()

# #     # Get the drone's magnetic heading from navdata.magneto.heading.fusionUnwrapped
# #     #mag_heading = drone.get_state(HomeChanged)["magneto"]["heading"]["fusionUnwrapped"]

    #the moveTo command send the drone to a certain coordinate point at a certain height
    #dummy values for now but this is the frame
    #lat and long should be x y and z minus the angle relative to 0,0,0
    print("moving to location")
    drone(moveBy(latitude, longitude, altitude).wait())

    assert drone(moveToChanged(_policy="check", _timeout=10)).wait()
    #set the gimbal to 45 degrees to capture the target
    assert drone(gimbal.set_target(gimbal_id=0, control_mode="position", 
                            yaw_frame_of_reference="none", yaw=0.0, pitch_frame_of_reference="absolute", pitch=45.0, 
                            roll_frame_of_reference="none", roll=0.0)).wait()
            
    drone(moveBy(0, 0, 0, math.radians(90))).wait()
    print("rotating")
    drone(moveBy(0, 0, 0, math.radians(-90))).wait()
    time.sleep(5)
    drone.ReturnHomeMinAltitude(50)
    drone(return_to_home()).wait()
    print("returning home")
    assert drone.disconnect()
    
    
def test_takeoff():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    gps_info = olympe.messages.controller_info.gps()
    print("GPS info: ", gps_info)
    drone.disconnect
    
if __name__ == "__main__":
    test_takeoff()
    #main()
    app.run(debug=True)
            
#from geofence import Point, Polygon

