export tag=latest
docker build \
-t pingpong:${tag} \
-f ./Dockerfile .
