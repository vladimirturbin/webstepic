sudo rm /etc/nginx/conf.d/*
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/conf.d/nginx.conf
sudo service nginx restart
