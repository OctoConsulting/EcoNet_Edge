echo "y" | docker container prune
echo "y" | docker image prune
docker image remove edge_db-db
docker image remove edge_db-dev
docker-compose up --build