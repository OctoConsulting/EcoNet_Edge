#!/bin/bash

# currently stops all ffmpegs, so it kills everything. Also removes all
# video files
# TODO: When we have multiple drones, that would be pretty bad.

pkill ffmpeg
