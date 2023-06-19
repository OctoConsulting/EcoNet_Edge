import cv2
import olympe
from olympe.messages import camera, streaming

# Initialize Olympe and the drone
drone = olympe.Drone("192.168.53.1")
drone.connection()

# Set up the video streaming
def handle_frame(frame):
    cv2.imshow("Live Video Feed", frame)
    cv2.waitKey(1)

drone.set_streaming_callbacks(raw_cb=handle_frame)

# Configure the video stream
drone.set_streaming_output_streams([
    streaming.video_streaming(port=8000),
    streaming.rtsp_streaming(port=8002)
])

# Start the video stream
drone.start_video_streaming()

# Wait for user interruption to stop the stream
input("Press Enter to stop the video streaming...\n")

# Stop the video stream
drone.stop_video_streaming()

# Disconnect from the drone
drone.disconnection()
cv2.destroyAllWindows()