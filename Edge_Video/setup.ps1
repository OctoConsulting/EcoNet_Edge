$ErrorActionPreference = "Stop" 
docker build -t vid_mk1 .
docker run -it --network="host" --mount type=bind,source="$env:USERPROFILE/Documents/GitHub/EcoNet_Edge",target=/mnt -p 8080:80 vid_mk1