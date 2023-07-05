#!/bin/bash
# does EVERYTHING
docker-compose down
echo "y" | docker container prune
echo "y" | docker image prune
docker-compose up --build