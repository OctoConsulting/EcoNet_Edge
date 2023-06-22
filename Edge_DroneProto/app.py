import olympe
import argparse
from flask import Flask, jsonify, request
import websocket
import json
import concurrent.futures
import os 
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
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

    else:
        print("idk")
    return jsonify({"message": "Command 'goodbye' processed."})
    
if __name__ == "__main__":
    #main()
    app.run(debug=True)
            
#from geofence import Point, Polygon

