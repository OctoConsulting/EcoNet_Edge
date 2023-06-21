import olympe 
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy 
from olympe.messages.ardrone3.PilotingState import (PositionChanged, AlertStateChanged, FlyingStateChanged, NavigateHomeStateChanged,)
import os
import time
# Connect to the drone
#if it doesnt work then you have to physically takeoff and call client.calibrate(0) once in the air

DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")

drone = olympe.Drone (DRONE_IP, drone_type=od.ARSDK_DEVICE_TYPE_ANAFI4K, mpp=True)
#drone(setPilotingSource(source=\"SkyController\")).wait()
class FlightListener(olympe.EventListener):
    @olympe.listen_event(FlyingStateChanged() | AlertStateChanged() | 
NavigateHomeStateChanged())
    def onStateChanged(self, event, scheduler):
        ...
    @olympe.listen_event(PositionChanged())
    def onPositionChanged(self, event, scheduler):
        ...
              
with FlightListener(drone):
    drone.connect()
    drone(set_home_position(38.945901, -77.315607, 0)).wait()
    drone.disconnect()


print("Latitude:", drone.get_state(PositionChanged)["latitude"])
print("Longitude:", drone.get_state(PositionChanged)["longitude"])
print("Altitude:", drone.get_state(PositionChanged)["altitude"])
