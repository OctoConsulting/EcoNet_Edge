# a nice script to test imports and takeoff
import olympe
import os
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged

# Connect to the drone
drone = olympe.Drone("192.168.53.1")
drone.connect()

gps_fix_info = drone(GPSFixStateChanged()).wait()

# Print the GPS fix information
print(gps_fix_info)


# Disconnect from the drone
drone.disconnect()


