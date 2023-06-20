#!/bin/bash

docker build -t dev_env_mk2 .
docker run -it --mount type=bind,source="$HOME/Documents/GitHub/EcoNet_Edge",target=/mnt --network host dev_env_mk2