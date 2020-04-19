sudo rm /etc/nginx/conf.d/*.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf

sudo rm /etc/gunicorn.d/wsgi.example
sudo rm /etc/gunicorn.d/django.example
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y python3.5

sudo apt-get install -y python3.5-dev

sudo unlink /usr/bin/python3

sudo ln -s /usr/bin/python3.5 /usr/bin/python3



# gunicorn --bind=0.0.0.0:8080 --workers=3 hello:application &

# sudo service nginx restart
