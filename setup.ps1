# does EVERYTHING
$ErrorActionPreference = "Stop"
docker-compose down
echo "y" | docker container prune
echo "y" | docker image prune
docker-compose up --build