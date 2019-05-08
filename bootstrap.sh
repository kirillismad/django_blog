#!/usr/bin/env bash

#python3.7
apt update
add-apt-repository ppa:deadsnakes/ppa
apt install -y python3.7

# alias
ln -s /usr/bin/python3.7 /usr/local/bin/python

# pip
apt install -y python3-pip

# python environment
apt install -y build-essential libssl-dev libffi-dev python3-dev python3.7-dev libpq-dev

# venv
apt install -y python3.7-venv

# postgresql
apt install -y postgresql postgresql-contrib

while IFS='' read -r line || [[ -n "$line" ]]; do
    su postgres -c "psql -c \"$line\" "
done < /vagrant/psql/docker-entrypoint-initdb.d/1step_db_init.sql

printf "localhost:*:django_blog:django_blog_user:password123" > /root/.pgpass
chmod 0600 /root/.pgpass

psql -U django_blog_user -h localhost django_blog -w < /vagrant/psql/dump.sql
rm /vagrant/psql/dump.sql


# memcached
apt install -y memcached


# rabbitmq
apt install -y rabbitmq-server
sudo rabbitmqctl add_user django_blog_user password123
sudo rabbitmqctl set_user_tags django_blog_user administrator
sudo rabbitmqctl set_permissions -p / django_blog_user ".*" ".*" ".*"
sudo systemctl restart rabbitmq-server


# install dependencies
python -m venv /home/vagrant/v_env
chown -R vagrant:vagrant /home/vagrant/v_env

ACTIVATE_ENV="/home/vagrant/v_env/bin/activate"
source $ACTIVATE_ENV
pip install -r /vagrant/src/requirements.txt
