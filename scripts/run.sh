#!/bin/bash

PROJECT_ROOT="$(cd "$(dirname "$0")"; cd ..; pwd)"
source ${PROJECT_ROOT}/config.sh

docker rm -f $CONTAINER_NAME
docker run --privileged --rm -it \
    -p 8888:8888 \
    --name $CONTAINER_NAME \
    --mount type=bind,source=${PROJECT_ROOT}/lessons,target=/control/lessons \
    ${DOCKER_IMAGE_NAME}
