docker build -t dev_env_mk1 .
docker run -it --mount type=bind,source="$env:USERPROFILE/Documents/GitHub/EcoNet_Edge",target=/mnt dev_env_mk1
