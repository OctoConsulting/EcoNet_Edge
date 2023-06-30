# file that encodes an rtsp stream into an hls stream (.m3u8).
# TODO: When we figure out a way to differentiate Parrot drones, we need to be
# able to pass in an argument --drone_number

#!/bin/bash

#ffmpeg -rw_timeout 5000000 -i "rtsp://192.168.53.1/live" \
#  -hls_time 3 -hls_wrap 10 "/usr/share/nginx/html/streaming.m3u8" #oldpath

ffmpeg -rw_timeout 5000000 -i "rtsp://192.168.53.1/live" \
  -hls_time 3 -hls_wrap 10 "/srv/feed1/streaming.m3u8"