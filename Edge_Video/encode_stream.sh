#!/bin/bash

# file that encodes an rtsp stream into an hls stream (.m3u8). Currently
# hardcoded to the default ip address of Parrot drones

# TODO: --drone_number argument for differentiating between drones
# TODO: detect if a stream is running for a certain drone, and do not start a
# new enode process

ffmpeg -i "rtsp://192.168.53.1/live"\
  -hls_time 3 -hls_wrap 10 -c copy "/srv/feed1/streaming.m3u8" &
cp ./index.html /srv/feed1/index.html # for reverse-proxy issues
