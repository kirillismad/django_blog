CREATE DATABASE django_blog;
CREATE USER django_blog_user WITH PASSWORD 'password123';
ALTER ROLE django_blog_user SET client_encoding TO 'utf8';
ALTER ROLE django_blog_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_blog_user SET timezone TO 'UTC';
GRANT ALL ON DATABASE django_blog TO django_blog_user;
ALTER USER django_blog_user CREATEDB;

