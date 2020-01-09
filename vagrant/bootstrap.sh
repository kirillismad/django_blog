#!/usr/bin/env bash

YQ="-y -q"
export DEBIAN_FRONTEND=noninteractive
apt update $YQ
apt upgrade $YQ

# prerequirements
apt install $YQ software-properties-common build-essential libssl-dev libffi-dev wget ca-certificates

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
su -c "printf 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main\n' >> /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt update $YQ
apt install $YQ postgresql-11 postgresql-contrib-11

while IFS='' read -r line || [[ -n "$line" ]]; do
    su postgres -c "psql -c \"$line\" "
done < /vagrant/vagrant/create_db.sql

printf "localhost:*:db:db_user:password123\n" > /root/.pgpass
chmod 0600 /root/.pgpass

# gettext
apt install $YQ gettext

# memcached
apt install $YQ memcached

# rabbitmq
apt install $YQ rabbitmq-server
sudo rabbitmqctl add_user broker_user password123
sudo rabbitmqctl set_user_tags broker_user administrator
sudo rabbitmqctl set_permissions -p / broker_user ".*" ".*" ".*"
sudo systemctl restart rabbitmq-server


# install dependencies
V_ENV="/home/vagrant/v_env"
ACTIVATE_ENV=$V_ENV/bin/activate

python -m venv $V_ENV
source $ACTIVATE_ENV
pip install --upgrade pip
pip install --requirement /vagrant/src/requirements.txt
printf "export DJANGO_SETTINGS_MODULE=blog.settings.dev\n" >> $ACTIVATE_ENV

chown -R vagrant:vagrant $V_ENV
