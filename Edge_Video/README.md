Video stream for the drone.

## Summary of files

**DockerfileHLS**

Where encoding, the flask interface and the nginx web server is run        

**app.py**

Flask interface. Includes a few apis:

/video/start_drone1

/video/stop_drone1

/video/start_drone2

/video/stop_drone2

/video/start_drone3

/video/stop_drone3

**encode_stream.sh**

encodes the rtsp stream into hls (m3u8)

**encode_vid.sh**

for testing purposes, encodes an existing video file into an hls stream while
looping the video.

**encode_stop.sh**

stops the stream

**container_startup.sh**

runs on container startup, starts the nginx and waitress servers

**nginx.conf**

Config for the NGINX server

**setup.ps1**

runs everything