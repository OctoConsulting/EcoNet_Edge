# a nice script to test imports and takeoff
import djisdkpy
import os
import time

DRONE_IP = os.environ.get("DRONE_IP", "192.168.42.81")
def test_takeoff():
    drone = djisdkpy.Drone('User.Config.txt')
    drone.initialize()
    time.sleep()
    drone.arm()
    drone.takeoff()
    time.sleep(5)
    drone.land()
    drone.disarm()
    drone.shutdown()
    ...


if __name__ == "__main__":

    test_takeoff()