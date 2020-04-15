sudo rm /etc/nginx/conf.d/*.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf

sudo rm /etc/gunicorn.d/wsgi.example
sudo rm /etc/gunicorn.d/django.example
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

sudo service nginx restart
