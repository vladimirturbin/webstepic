#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

sudo rm /etc/nginx/conf.d/*.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf

sudo rm /etc/gunicorn.d/wsgi.example
sudo rm /etc/gunicorn.d/django.example
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart


sudo add-apt-repository ppa:deadsnakes/ppa -Y
sudo apt-get update 
sudo apt-get upgrade -Y
sudo apt-get install python3.6-dev python3.6-venv -Y

python3.6 -m venv ~/myvenv
source ~/myvenv/bin/activate

pip3 install -U pip
pip3 install -U setuptools
pip3 install django

# gunicorn --bind=0.0.0.0:8080 --workers=3 hello:application &

# sudo service nginx restart
