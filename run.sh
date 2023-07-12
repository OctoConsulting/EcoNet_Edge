#!/bin/bash

# script that runs the whole program and logs the output
docker-compose down
docker-compose up > "$(date +"%Y-%m-%d_%H-%M-%S")_run.log"
