# a nice script to test imports and takeoff
import olympe
import os
import time

DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1")
def test_takeoff():

    drone = olympe.Drone(DRONE_IP)

    drone.connect()

    assert drone(TakeOff()).wait().success()

    time.sleep(10)

    assert drone(Landing()).wait().success()

    drone.disconnect()



if __name__ == "__main__":

    test_takeoff()