# a nice script to test imports and takeoff
import olympe
import os
import time
from olympe.messages.ardrone3.PilotingState import PositionChanged

# Connect to the drone
drone = olympe.Drone("192.168.53.1")
drone.connect()

# Print the latitude and longitude of the drone
print("Latitude:", drone.get_state(PositionChanged)["latitude"])
print("Longitude:", drone.get_state(PositionChanged)["longitude"])

# Disconnect from the drone
drone.disconnect()


