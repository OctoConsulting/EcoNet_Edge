# a nice script to test imports and takeoff
import olympe
import os
import time
# Connect to the drone
from olympe.messages.ardrone3.PilotingState import GpsLocationChanged
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged

DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
drone = olympe.Drone(DRONE_IP)
drone.connect()

def gps_callback(self, latitude, longitude, altitude):
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Altitude:", altitude)

drone(GPSLocationChanged(_policy = 'wait', _no_expect = True)). \
    each(gps_callback). \
    wait()

