#!/bin/bash

set -e

source ./.env

COMPOSE_PROJECT_NAME=${PROJECT_NAME}

docker compose -p ${COMPOSE_PROJECT_NAME} up -d
