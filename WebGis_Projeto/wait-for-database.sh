#!/bin/bash

set -e

host="$1"
shift

until PGPASSWORD=${PG_PASSWORD} psql -h "$host" -U ${PG_USERNAME} -P "pager=off" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

until PGPASSWORD=${PG_PASSWORD} psql -h "$host" -U ${PG_USERNAME} -P "pager=off" -c '\l'; do
  >&2 echo " is unavailable - sleeping"
  sleep 1
done

until PGPASSWORD=${PG_PASSWORD} psql -h "$host" -U ${PG_USERNAME} -P "pager=off" -c '\l'; do
  >&2 echo " is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL databases are up - executing command"
