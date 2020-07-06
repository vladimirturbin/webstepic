#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# This init script is for installing and starting my web project from stepik 
# web programming course on elder (ubuntu 14/04) OS

echo "mysql-server-5.6 mysql-server/root_password password ok" | sudo debconf-set-selections
echo "mysql-server-5.6 mysql-server/root_password_again password ok" | sudo debconf-set-selections

sudo apt-get update
sudo apt install nginx mysql-server-5.6 libmysqlclient-dev -y

sudo service mysql start

sudo rm -f /etc/nginx/conf.d/*.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf

sudo rm -f /etc/gunicorn.d/wsgi.example
sudo rm -f /etc/gunicorn.d/django.example

#set +e
#mysql -u root -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('ok');"
#set -e

mysql -u root -pok -e "GRANT ALL PRIVILEGES ON *.* TO 'sa'@'localhost' IDENTIFIED BY 'zR8adKkCy22ANKW5.';"
mysql -u sa -pzR8adKkCy22ANKW5. -e "CREATE DATABASE askdb;"
mysql -u sa -pzR8adKkCy22ANKW5. askdb < ~/web/etc/dump.txt

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update 
# sudo apt-get upgrade -y
sudo apt-get install python3.6-dev python3.6-venv -y

python3.6 -m venv ~/myvenv
source ~/myvenv/bin/activate

pip3 install --timeout 120 -U pip setuptools
pip3 install --timeout 120 wheel django gunicorn mysqlclient

#gunicorn --bind=0.0.0.0:8080 --chdir ~/web/ --workers=3 hello:application &
gunicorn --bind=0.0.0.0:8000 --chdir ~/web/ask/ --workers=3 ask.wsgi --access-logfile gunicorn.log &

mysql -u root -pok -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('Yg6dGdfZa3K6y3ae');"

sudo service nginx restart
