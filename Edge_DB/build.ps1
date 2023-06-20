docker-compose down
echo "y" | docker container prune
echo "y" | docker image prune
docker image remove edge_db-db
docker image remove edge_db-dev
docker-compose up --build -d
Start-Sleep -Seconds 5
docker exec -it $(docker ps -aqf "name=db-dev") python3 test_init.py