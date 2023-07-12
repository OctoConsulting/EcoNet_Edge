#!/bin/bash

# currently stops all ffmpegs, so it kills everything. Also removes all
# video files
# TODO: When we have multiple drones, that would be pretty bad.

pkill ffmpeg
#rm /var/www/html/streaming.m3u8
#rm /var/www/html/*.ts