#!/bin/bash

ffmpeg -i "rtsp://192.168.53.1/live" -hls_time 3 -hls_wrap 10 "/usr/share/nginx/html/streaming.m3u8"
ffmpeg -re -stream_loop -1 -i video.mp4 -hls_time 3 -hls_wrap 10 -c copy streaming.m3u8