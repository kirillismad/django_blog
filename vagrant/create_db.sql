CREATE DATABASE db;
CREATE USER db_user WITH PASSWORD 'password123';
ALTER ROLE db_user SET client_encoding TO 'utf8';
ALTER ROLE db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE db_user SET timezone TO 'UTC';
GRANT ALL ON DATABASE db TO db_user;
ALTER USER db_user CREATEDB;

