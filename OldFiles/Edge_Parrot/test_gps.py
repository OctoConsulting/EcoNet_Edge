import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from olympe.messages.ardrone3.PilotingState import PositionChanged
from olympe.media.GPS

# Create the Olympe.Drone object from its IP address
drone = olympe.Drone("192.168.42.1")

# Connect to the drone
drone.connect()

# Take off
drone(TakeOff()).wait()

# Calibrate the magnetometer
#drone.calibrate(0)

# Get the drone's magnetic heading from navdata.magneto.heading.fusionUnwrapped
mag_heading = drone.get_state(HomeChanged)["magneto"]["heading"]["fusionUnwrapped"]

# Get the drone's current coordinates from navdata.gps.latitude and navdata.gps.longitude
latitude = drone.get_state(PositionChanged)["latitude"]
longitude = drone.get_state(PositionChanged)["longitude"]

print("Latitude: {latitude}")
print("Longitude: {longitude}")

# Land
drone(Landing()).wait()

# Disconnect from the drone
drone.disconnect()