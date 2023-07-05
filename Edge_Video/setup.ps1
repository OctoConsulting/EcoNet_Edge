$ErrorActionPreference = "Stop"
docker-compose down
echo "y" | docker container prune
echo "y" | docker image prune
docker image remove edge_video-web
docker-compose up --build -d
Start-Sleep -Seconds 5
docker exec -it $(docker ps -aqf "name=edge_video-web") bash container_startup.sh