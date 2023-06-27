#!/bin/bash

ffmpeg -re -stream_loop -1 -i test_vid.mp4 -hls_time 3 -hls_wrap 10 -c copy /usr/share/nginx/html/streaming.m3u8