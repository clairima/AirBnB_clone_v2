#!/usr/bin/env bash
# Install Nginx if not already installed
    
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html

echo "<html><head><title>Test Page</title></head><body><p>This is a test page.</p></body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^server {/a \
\\tlocation /hbnb_static/ {\
\\t\\talias /data/web_static/current/;\
\\t}\\
' $nginx_config

sudo service nginx restart
