#!/bin/bash

docker build -t dev_env_mk1 .
docker run -it --mount type=bind, source="../../", target=/mnt dev_env_mk1