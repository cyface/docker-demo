docker build --tag cyface/docker-demo:latest --no-cache .
docker login
docker push cyface/docker-demo:latest