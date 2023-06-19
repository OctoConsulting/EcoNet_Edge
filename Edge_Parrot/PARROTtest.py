#import cv2
import olympe
from olympe import *
import os
from olympe.messages.ardrone3.Piloting import TakeOff, Landing

#from olympe import stream

# Initialize Olympe and the drone

DRONE_IP = os.environ.get("DRONE_IP", "192.168.53.1")

drone = olympe.Drone(DRONE_IP)

hello = drone.connect(retry= 3)
#drone.takeoff()
#drone(TakeOff()).wait().success()
#time.sleep(10)
drone(Landing()).wait().success()
drone.disconnect()
#print("true", hello)
#drone.fly()
#def handle_frame(frame):
#    cv2.imshow("Live Video Feed", frame)
#    cv2.waitKey(1)

#ctrl u to undo ctrl k to eray
#drone.set_stream_callbacks(raw_cb=handle_frame)
# Configure the video stream
drone.set_stream_output_streams([
    streaming.video_streaming(port=8000),
    streaming.rtsp_streaming(port=8002)
])

# Start the video stream
drone.start_video_stream()

# Wait for user interruption to stop the stream
input("Press Enter to stop the video streaming...\n")

# Stop the video stream
drone.stop_video_stream()

# Disconnect from the drone
drone.disconnection()
cv2.destroyAllWindows()


#olympe.Pdraw("rtsp://192.168.42.1/live")
