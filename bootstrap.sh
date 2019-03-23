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
done < /vagrant/db_init.sql

python -m venv /home/vagrant/v_env
chown -R vagrant:vagrant /home/vagrant/v_env