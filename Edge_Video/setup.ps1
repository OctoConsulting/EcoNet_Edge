# sets up containers for video
$ErrorActionPreference= "Stop"

docker-compose down

# clear cached videos from the previous run
Write-Output "y" | docker container prune

docker image remove edge_video-web
docker-compose up --build
