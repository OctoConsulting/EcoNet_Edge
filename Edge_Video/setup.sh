#!/bin/bash
# sets up containers for video
set -u
set -x
set -e

docker-compose down

# clear cached videos from the previous run
echo "y" | docker container prune 

docker-compose up --build
