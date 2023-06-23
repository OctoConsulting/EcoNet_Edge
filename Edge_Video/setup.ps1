$ErrorActionPreference = "Stop" 
# docker build -f DockerfileHLS . vid_mk1
# docker run -it --network="host" --mount `
# type=bind,source="$env:USERPROFILE/Documents/GitHub/EcoNet_Edge",target=/mnt `
# -p 8088:8088 vid_mk1
docker-compose up --build