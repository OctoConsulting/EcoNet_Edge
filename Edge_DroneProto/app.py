# import olympe
# from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy
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

def worker(commands):
    #here parse the commands and fitures of what our functiioons to run to send infor to the drone

    target = commands['DroneType']
    ip_address = commands['DroneIP']
    lon = commands['LONG']
    lat = commands['LAT']
    # physical_port = args.physical_port


    if target == "skydio":
        # Skydio drone code here
        pass


    elif target == "parrot":
        with Olympe() as drone:
            drone.connect()
            latitude = lat
            longitude = lon
            altitude = 20
            geofence_size = 0.01
            drone.start()

            #the moveTo command send the drone to a certain coordinate point at a certain height
            #dummy values for now but this is the frame
            drone.disconnect()


@sock.route('/protocal', methods=['GET'])
def managage_commands(ws):
    
    try:
        while True:
            # reciving data structure
            # json object
            # params = {
            #     "DroneType": "parrot",
            #     "DRONE_IP": "hello",
            #     "LONG": "223.2",
            #     "LAT": "2232"
            # }

            data = ws.receive()
            data_loaded = json.loads(data)
            
            print(data_loaded)
            
            # submit tasks to the pool
            pool.submit(worker, data_loaded)

            m = {"message": "thread sent to work"}
            ws.send(json.dumps(m))
            
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        pass

    return jsonify({"message": "connection closed"})



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

    
# DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
# # def test_find():
# #     drone = olympe.Drone(DRONE_IP)
# #     drone.connect()
# #     drone.start()
# #     altitude = 50
# #     latitude = drone.get_state(PositionChanged)["latitude"])
# #     longitude = drone.get_state(PositionChanged)["longitude"])

# #     drone(TakeOff()).wait()

# #     # Calibrate the magnetometer 
# #     #temporary fix
# #     drone.calibrate(0)

# #     # Get the drone's magnetic heading from navdata.magneto.heading.fusionUnwrapped
# #     #mag_heading = drone.get_state(HomeChanged)["magneto"]["heading"]["fusionUnwrapped"]

# #     #the moveTo command send the drone to a certain coordinate point at a certain height
# #     #dummy values for now but this is the frame
# #     drone(moveTo(latitude, longitude, altitude).wait())
# #     #set the gimbal to 45 degrees to capture the target
# #     drone(gimbal.set_target(gimbal_id=0, control_mode="position", 
# #                             yaw_frame_of_reference="none", yaw=0.0, pitch_frame_of_reference="absolute", pitch=45.0, 
# #                             roll_frame_of_reference="none", roll=0.0)).wait()
            
# #     drone(moveBy(0, 0, 0, math.radians(90))).wait()
# #     drone(moveBy(0, 0, 0, math.radians(-90))).wait()
# #     drone.disconnect()
    
    
# def test_takeoff():
#     drone = olympe.Drone(DRONE_IP)
#     drone.connect()
#     assert drone(TakeOff()).wait().success()
#     time.sleep(5)
#     assert drone(Landing()).wait().success()
#     drone.disconnect
    
if __name__ == "__main__":
    #main()
    app.run(debug=True)
            
#from geofence import Point, Polygon

