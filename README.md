
# Deploying manual (Ubuntu clean server)

    $ apt update && apt upgrade
 
###### Rnning as root is bad practice. Let's create a user for further work

    $ sudo adduser astorun 
    $ sudo usermod -aG sudo astorun
    $ groups astorun
    $ su astorun
    
###### Great now install programs for our site settings    

    $ cd && sudo apt install nginx git supervisor postgresql
    
###### Database configuration

    $ sudo -u postgres psql
    $ CREATE DATABASE astorun;
    $ CREATE USER the_astoruner WITH PASSWORD 'astorun';
    $ ALTER ROLE the_astoruner SET client_encoding TO 'utf8';
    $ ALTER ROLE the_astoruner SET default_transaction_isolation TO 'read committed';
    $ ALTER ROLE the_astoruner SET timezone TO 'UTC';
    $ GRANT ALL PRIVILEGES ON DATABASE astorun TO the_astoruner;
    $ \q
    
###### And thats it for DB. Now let's make a virtual environment for our site

    $ curl -sSL https://install.python-poetry.org | python3 -
    $ sudo ln -s /home/astorun/.local/bin/poetry /usr/bin/poetry
    $ poetry --version
    
###### And we are inside of virtual environment
We can clone project here from github, make directorys for static files directly and install all dependencies

    $ git clone https://...
    $ sudo chown -R $USER:$USER astorun_2022
    $ cd astorun_2022

    $ poetry shell
    $ poetry install
    $ mkdir media
    $ mkdir static
    
    
###### Now we have everything to create our tables in database and create an administrator

    $ poetry run python manage.py makemigrations
    $ poetry run python manage.py migrate

###### create basic data (statuses, categories, docs)    
    $ poetry run python manage.py runscript create_basic
    $ poetry run python manage.py collectstatic
    $ poetry run python manage.py createsuperuser
    
### Nginx 

###### check ports

    $ sudo ufw status verbose

###### port 80 and 443 must be opened. If not do next:
    $ sudo ufw allow http
    $ sudo ufw allow https

###### settings (we can copy settings files from our project)
    $ cp /home/zxc/astorun_2022/nginx/astorun.conf /etc/nginx/sites-available/
    $ ln -s /etc/nginx/sites-available/astorun.conf /etc/nginx/sites-enabled/

###### [optional] you can also setup cache, firewall or logs file. Change settings in /etc/nginx/nginx.conf
look example at /astorun_2022/nginx/nginx.conf
    
###### SSL certificate for https requests

    $ sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
    $ mkdir -p /etc/nginx/snippets/
    $ sudo nano /etc/nginx/snippets/ssl-params.conf
    
###### And just paste next 

    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;

    ssl_dhparam /etc/ssl/certs/dhparam.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    add_header Strict-Transport-Security "max-age=63072000" always;
    
###### Make certificate with certbot and restart nginx

    $ sudo snap install core
    $ sudo snap install --classic certbot
    $ sudo ln -s /snap/bin/certbot /usr/bin/certbot
    $ sudo certbot certonly --nginx
    $ sudo systemctl restart nginx

###### Sertificate available for 90 days, but we can provide auto renew (do it as root)

    $ crontab -e
    $ @daily certbot renew
    
###### And at last we need to enable supervisor

    $ cd /etc/supervisor/conf.d
    $ sudo ln /home/astorun/astorun_2022/config/astorun.conf
    ***
    $ whereis gunicorn

###### copy outout into astorun.conf (command=<path>) 

    $ sudo update-rc.d supervisor enable
    $ sudo service supervisor start
    $ sudo supervisorctl reread
    $ sudo supervisorctl update
    $ sudo supervisorctl status

###### If output is

    astorun: RUNNING

###### Congratulation, our site is working!

    



    

