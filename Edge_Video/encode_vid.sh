#!/bin/bash

#cp ./index.html /srv/feed1/index.html

ffmpeg -re -stream_loop -1 -i test_vid.mp4 -hls_time 3 -hls_wrap 10 -c copy /srv/feed1/streaming.m3u8 &