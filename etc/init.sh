#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

sudo rm -f /etc/nginx/conf.d/*.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf

sudo rm -f /etc/gunicorn.d/wsgi.example
sudo rm -f /etc/gunicorn.d/django.example
# sudo ln -sf ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop


sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update 
# sudo apt-get upgrade -y
sudo apt-get install python3.6-dev python3.6-venv -y

python3.6 -m venv ~/myvenv
source ~/myvenv/bin/activate

pip3 install -U pip
pip3 install -U setuptools
pip3 install django 

gunicorn --bind=0.0.0.0:8080 --chdir ~/web/ --workers=3 hello:application &

sudo service nginx restart
