import olympe
import argparse
from flask import Flask, jsonify, request

#from geofence import Point, Polygon

def parrot_intake():
    pass


def skydio_intake():
    pass

 

def setup_geofence(drone, latitude, longitude, geofence_size):
    geofence_coordinates = [doc
        {
            "latitude": latitude + geofence_size,
            "longitude": longitude + geofence_size
        },
        {
            "latitude": latitude + geofence_size,
            "longitude": longitude - geofence_size
        },
        {
            "latitude": latitude - geofence_size,
            "longitude": longitude - geofence_size
        },
        {
            "latitude": latitude - geofence_size,
            "longitude": longitude + geofence_size
        }
    ]

 

    geofence = Geofence(geofence_coordinates)
    drone(Geofence.geofence_set(geofence))
    drone.subscribe(
        Geofence.ViolationStateChangedEvent(on_geofence_violation),
        safe=True
    )

 

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
            setup_geofence(drone, latitude, longitude, geofence_size)
            drone.start()

            #the moveTo command send the drone to a certain coordinate point at a certain height
            #dummy values for now but this is the frame
            drone(moveTo(latitude, longitude, altitude).wait())
            drone.disconnect()

 

    else:
        print("Drone type not supported")

app = Flask(__name__)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Drone Connection Script')
    # parser.add_argument('-t', '--target', type=str, help='Specify the target')
    # parser.add_argument('-i', '--ip_address', type=str, help='Specify the IP address')
    # parser.add_argument('-p', '--physical_port', type=int, help='Specify the physical port')
    # parser.add_argument('-lon', '--lon', type=int, help='Specify Longitude')
    # parser.add_argument('-lat', '--lat', type=int, help='Specify Latitude')

 

    # args = parser.parse_args()
    # main(args)
    app.run()
