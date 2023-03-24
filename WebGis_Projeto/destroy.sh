#!/bin/bash

set -e

. .env

COMPOSE_PROJECT_NAME=${PROJECT_NAME}

docker compose -p ${COMPOSE_PROJECT_NAME} down -v
docker rmi $(docker images | grep webgis | awk '{print $3}')
