#!/usr/bin/env bash

YQ="-y -q"
export DEBIAN_FRONTEND=noninteractive

# prerequirements
apt install $YQ software-properties-common python-software-properties build-essential libssl-dev libffi-dev wget ca-certificates

#python3.7
apt update $YQ
add-apt-repository ppa:deadsnakes/ppa
apt install $YQ python3.7

# alias
ln -s /usr/bin/python3.7 /usr/local/bin/python

# pip
apt update $YQ
apt install $YQ python3-pip

# python environment
apt install $YQ python3-dev python3.7-dev libpq-dev

# venv
apt install $YQ python3.7-venv

# postgresql
su -c "printf 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' >> /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
sudo apt update $YQ
sudo apt install $YQ postgresql postgresql-contrib

while IFS='' read -r line || [[ -n "$line" ]]; do
    su postgres -c "psql -c \"$line\" "
done < /vagrant/psql/docker-entrypoint-initdb.d/1step_db_init.sql

printf "localhost:*:django_blog:django_blog_user:password123" > /root/.pgpass
chmod 0600 /root/.pgpass

psql -U django_blog_user -h localhost django_blog -w < /vagrant/psql/dump.sql

# memcached
apt install $YQ memcached


# rabbitmq
apt install $YQ rabbitmq-server
sudo rabbitmqctl add_user django_blog_user password123
sudo rabbitmqctl set_user_tags django_blog_user administrator
sudo rabbitmqctl set_permissions -p / django_blog_user ".*" ".*" ".*"
sudo systemctl restart rabbitmq-server


# install dependencies
python -m venv /home/vagrant/v_env
chown -R vagrant:vagrant /home/vagrant/v_env

ACTIVATE_ENV="/home/vagrant/v_env/bin/activate"
source $ACTIVATE_ENV
pip install --upgrade pip
pip install -r /vagrant/src/requirements.txt
