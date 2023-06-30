#!/bin/bash

docker build -t api .
docker run -it --device /dev/snd api /bin/bash
