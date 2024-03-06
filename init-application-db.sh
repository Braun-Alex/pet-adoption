#!/bin/bash
set -e

execute_sql() {
    psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname "${POSTGRES_DB}" -c "$1"
}

DB_EXISTS=$(psql -U "${POSTGRES_USER}" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='${POSTGRES_DB}'")
if [ "$DB_EXISTS" != "1" ]; then
    execute_sql "CREATE DATABASE \"${POSTGRES_DB}\""
fi

ROLE_EXISTS=$(psql -U "${POSTGRES_USER}" -d postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='${POSTGRES_USER}'")
if [ "$ROLE_EXISTS" != "1" ]; then
    execute_sql "CREATE ROLE \"${POSTGRES_USER}\" WITH LOGIN PASSWORD '${POSTGRES_PASSWORD}'"
fi

execute_sql "CREATE TYPE application_status AS ENUM ('REJECTED', 'ACCEPTED', 'CREATED');"

psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" <<-EOSQL
    CREATE TABLE IF NOT EXISTS applications (
        id SERIAL PRIMARY KEY NOT NULL,
        shelter_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        animal_id INTEGER NOT NULL,
        status application_status DEFAULT 'CREATED'
    );
EOSQL

psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "ALTER TABLE applications OWNER TO \"${POSTGRES_USER}\""
