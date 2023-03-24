#!/bin/bash

set -e

. .env

COMPOSE_PROJECT_NAME=${PROJECT_NAME}

docker compose -p ${COMPOSE_PROJECT_NAME} down
docker compose -p ${COMPOSE_PROJECT_NAME} up --build -d
