#!/bin/bash

ffmpeg -rw_timeout 5000000 -i "rtsp://192.168.53.1/live" -hls_time 3 -hls_wrap 10 "/usr/share/nginx/html/streaming.m3u8"