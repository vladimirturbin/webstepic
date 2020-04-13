sudo rm /etc/nginx/conf.d/*.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf
sudo service nginx restart
