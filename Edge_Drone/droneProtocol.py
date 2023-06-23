import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy
from olympe.messages.ardrone3.PilotingSettingsState import Geofence
from olympe.messages.ardrone3.PilotingState import PositionChanged
from olympe.messages import gimbal
import argparse
import math
#from geofence import Point, Polygon
#recieving coordinates, drone type, 

def parrot_intake():
    pass


def skydio_intake():
    pass


def setup_geofence(drone, latitude, longitude, geofence_size):
    geofence_coordinates = [
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
            altitude = 50
            geofence_size = 0.01
            setup_geofence(drone, latitude, longitude, geofence_size)
            drone.start()

            drone(TakeOff()).wait()

            # Calibrate the magnetometer 
            #temporary fix
            drone.calibrate(0)

            # Get the drone's magnetic heading from navdata.magneto.heading.fusionUnwrapped
            mag_heading = drone.get_state(HomeChanged)["magneto"]["heading"]["fusionUnwrapped"]

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

 

    else:
        print("Drone type not supported")

 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Drone Connection Script')
    parser.add_argument('-t', '--target', type=str, help='Specify the target')
    parser.add_argument('-i', '--ip_address', type=str, help='Specify the IP address')
    parser.add_argument('-p', '--physical_port', type=int, help='Specify the physical port')
    parser.add_argument('-lon', '--lon', type=int, help='Specify Longitude')
    parser.add_argument('-lat', '--lat', type=int, help='Specify Latitude')

 

    args = parser.parse_args()
    main(args)