docker build --no-cache .
docker tag docker-demo cyface/docker-demo:latest
docker login
docker push cyface/docker-demo:latest