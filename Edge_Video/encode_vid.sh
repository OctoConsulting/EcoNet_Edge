#!/bin/bash

# a file to start encoding the test stream found in test_vid.mp4
# It encodes it as an HLS in a loop forever

ffmpeg -re -stream_loop -1 -i test_vid.mp4 \
  -hls_time 3 -hls_wrap 10 -c copy /srv/feed1/streaming.m3u8 &
cp ./index.html /srv/feed1/index.html # for reverse-proxy issues
