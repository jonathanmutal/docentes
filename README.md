# odoo-module
Building a new module for odoo's framework.

---------------------
## Locally installation

### Installing the database's manager
    $ sudo apt install postgresql

### Installing odoo framework.

Download .deb file (you must fill a form) https://www.odoo.com/es_ES/page/download and install it.


### Setting-up the database.

    $ sudo su postgres
    $ psql
    $ create user odoo password '12345';
    $ create database odoo with owner odoo;
    $ grant all privileges on database odoo to odoo;

### Odoo's configuration file.

The /etc/odoo/odoo.config (create if it doesn't exist) should be like this:

<p align="left">
[options] <br>
; This is the password that allows database operations: <br>
; admin_passwd = admin <br>
db_host = localhost <br>
db_port = 5432 <br>
db_user = odoo <br>
db_password = 12345 <br>
;addons_path = /usr/lib/python3/dist-packages/odoo/addons <br>
</p>

### Restarting all the services

    $ sudo service postgresql restart
    $ sudo service odoo restart

### Installing the module
Clone this repo and add it to addons_path (if you follow the instructons, It may be /usr/lib/python3/dist-packages/odoo/addons). After that, restarting odoo's servicies.

### Runing
Enter in localhost:8069 from a browser. The first time it a little bit slow.

When odoo's logo show up, it's ready!. Well, the credentials are:

User: admin <br>
Pass: admin
