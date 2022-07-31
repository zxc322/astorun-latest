
# Ubuntu clean server manual

    $ apt update && apt upgrade
 
###### Rnning as root is bad practice. Let's create a user for further work

    $ sudo adduser astorun 
    $ sudo usermod -aG sudo astorun
    $ groups astorun
    $ su astorun

