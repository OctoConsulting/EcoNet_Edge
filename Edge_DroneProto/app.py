import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy
from olympe.messages.ardrone3.PilotingSettingsState import Geofence
from olympe.messages.ardrone3.PilotingState import PositionChanged
from olympe.messages import gimbal
import argparse
from flask import Flask, jsonify, request
import websocket
import json
import concurrent.futures
import os 
import time
import math
num_of_drones = 3 


app = Flask(__name__)
def parrot_intake():
    pass
def skydio_intake():
    pass
def main(args):
    target = args.target
    ip_address = args.ip_address
    physical_port = args.physical_port
    lon = args.lon
    lat = args.lat

 

    if target == "skydio":
        with Olympe() as drone:
            drone.connect(ip_address)
            # Skydio drone code here

 

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

 

    else:
        print("Drone type not supported")



#if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Drone Connection Script')
    # parser.add_argument('-t', '--target', type=str, help='Specify the target')
    # parser.add_argument('-i', '--ip_address', type=str, help='Specify the IP address')
    # parser.add_argument('-p', '--physical_port', type=int, help='Specify the physical port')
    # parser.add_argument('-lon', '--lon', type=int, help='Specify Longitude')
    # parser.add_argument('-lat', '--lat', type=int, help='Specify Latitude')

 

    # args = parser.parse_args()
    # main(args)
    #app.run()
def worker(commands):
    print("worker thread is running")
    #here parse the commands and fitures of what our functiioons to run to send infor to the drone
    
def main():
    ws = websocket.websocket()
    ws.connect("ws://manger:5000")
    
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=num_of_drones)
    
    try:
        while True:
            
            
            data = ws.receive()
            data_loaded = json.loads(data)
            
            print(data_loaded)
            
            #submit task to the pool
            pool.submit(worker, data_loaded)
            
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()
    
DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
def test_find():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    drone.start()
    altitude = 50
    latitude = drone.get_state(PositionChanged)["latitude"])
    longitude = drone.get_state(PositionChanged)["longitude"])

    drone(TakeOff()).wait()

    # Calibrate the magnetometer 
    #temporary fix
    drone.calibrate(0)

    # Get the drone's magnetic heading from navdata.magneto.heading.fusionUnwrapped
    #mag_heading = drone.get_state(HomeChanged)["magneto"]["heading"]["fusionUnwrapped"]

    #the moveTo command send the drone to a certain coordinate point at a certain height
    #dummy values for now but this is the frame
    drone(moveTo(latitude, longitude, altitude).wait())
    #set the gimbal to 45 degrees to capture the target
    drone(gimbal.set_target(gimbal_id=0, control_mode="position", 
                            yaw_frame_of_reference="none", yaw=0.0, pitch_frame_of_reference="absolute", pitch=45.0, 
                            roll_frame_of_reference="none", roll=0.0)).wait()
            
    drone(moveBy(0, 0, 0, math.radians(90))).wait()
    drone(moveBy(0, 0, 0, math.radians(-90))).wait()
    drone.disconnect()
    
    
def test_takeoff():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    assert drone(TakeOff()).wait().success()
    time.sleep(10)
    assert drone(Landing()).wait().success()
    drone.disconnect

@app.route("/api/command", methods=["GET"])
def process_command():
    command = request.json.get("content")
    print(command)
    #test_takeoff()
    
    if command == "hello":
        print("recieved")
        return jsonify({"message": "Command 'goodbye' processed."})
    elif command == "parrot":
        print("running test find")
        test_find()
        return jsonify({"message": "Command 'test_find processed."})

    else:
        print("idk")
    return jsonify({"message": "Command 'goodbye' processed."})
    
if __name__ == "__main__":
    #main()
    app.run(debug=True)
            
#from geofence import Point, Polygon

