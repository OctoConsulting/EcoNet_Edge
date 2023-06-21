# a nice script to test imports and takeoff
import olympe
import os
import time
# Connect to the drone
from olympe.messages.ardrone3.PilotingState import GpsLocationChanged
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged

DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
drone = olympe.Drone(DRONE_IP)
drone.connection()

# Wait for GPS fix before receiving GPS data
drone(GPSFixStateChanged(_policy='wait'))

print(drone.get_state(GpsLocationChanged))

print("Latitude:", drone.get_state(GpsLocationChanged)["latitude"])
print("Longitude:", drone.get_state(GpsLocationChanged)["longitude"])
print("Altitude:", drone.get_state(GpsLocationChanged)["altitude"])

