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
done < /vagrant/psql/docker-entrypoint-initdb.d/db_init.sql

# memcached
apt install -y memcached


# rabbitmq
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
dpkg -i erlang-solutions_1.0_all.deb
apt -y update
apt install -y erlang erlang-nox
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
apt -y update
apt install -y rabbitmq-server
sudo rabbitmqctl add_user django_blog_user password123
sudo rabbitmqctl set_user_tags django_blog_user administrator
sudo rabbitmqctl set_permissions -p / django_blog_user ".*" ".*" ".*"
sudo systemctl restart rabbitmq-server



python -m venv /home/vagrant/v_env
chown -R vagrant:vagrant /home/vagrant/v_env