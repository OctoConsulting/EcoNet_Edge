import olympe 
from olympe.messages.ardrone3.Piloting import NavigateHome
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
from olympe.messages.ardrone3.PilotingState import (PositionChanged, AlertStateChanged, FlyingStateChanged, NavigateHomeStateChanged,)
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged
import os
import time
# Connect to the drone
#if it doesnt work then you have to physically takeoff and call client.calibrate(0) once in the air

DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")
drone = olympe.Drone(DRONE_IP)
drone.connect()

drone(GPSFixStateChanged(latitude=37.4219983, longitude=-122.084))

print("Latitude:", drone.get_state(PositionChanged)["latitude"])
print("Longitude:", drone.get_state(PositionChanged)["longitude"])
print("Altitude:", drone.get_state(PositionChanged)["altitude"])

drone.disconnect()