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

psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" <<-EOSQL
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        salt VARCHAR(255) NOT NULL,
        photo VARCHAR(255) NULL,
        description TEXT NULL
    );
EOSQL

psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "ALTER TABLE users OWNER TO \"${POSTGRES_USER}\""
