
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

    $ sudo apt-get install python3-venv
    $ python3 -m venv venv
    $ cd && source venv/bin/activate

    ### install poetry instead
    
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

    $ cd astorun_2022
    $ poetry run python manage.py makemigration
    $ poetry run python manage.py migrate

###### create basic data (statuses, categories, docs)    
    $ poetry run python manage.py runscript create_basic
    $ poetry run python collectstatic
    $ poetry run python createsuperuser
    
###### Nginx settings (we can copy settings files from our project)

    $ cp /home/zxc/astorun_2022/nginx/astorun.conf /etc/nginx/sites-available/
    $ ln -s /etc/nginx/sites-available/astorun.conf /etc/nginx/sites-enabled/

    ###### also look at /astorun_2022/nginx/nginx.conf (make changes what you need in /etc/nginx/nginx.conf)
    
###### SSL certificate for https requests

    $ openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
    $ mkdir -p /etc/nginx/snippets/
    $ nano /etc/nginx/snippets/ssl-params.conf
    
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

    $ snap install core
    $ snap install --classic certbot
    $ sudo ln -s /snap/bin/certbot /usr/bin/certbot
    $ certbot certonly --nginx
    $ sudo systemctl restart nginx
    
###### And at last we need to enable supervisor

    $ cd /etc/supervisor/conf.d
    $ sudo ln /home/zxc/astorun_2022/config/astorun.conf
    ***
    $ sudo update-rc.d supervisor enable
    $ sudo service supervisor start
    $ sudo supervisorctl reread
>If output

    astorun: available
>Do next

    $ sudo supervisorctl update
    $ sudo supervisorctl status

###### If output is

    astorun: RUNNING

###### Congratulation, our site is working!

    



    

