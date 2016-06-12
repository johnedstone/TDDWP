Provisioning a new site
======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

e.g., on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

    sed "s/SITENAME/superlist.johnedstone-ec2.net/g" sites/superlist.johnedstone-ec2.net/source/deploy_tools/nginx.template.conf  | sudo tee /etc/nginx/sites-available/superlist.johnedstone-ec2.net 

    sudo ln -s /etc/nginx/sites-available/superlist.johnedstone-ec2.net /etc/nginx/sites-enabled/


## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with e.g., stagin.my-domain.com

    sed 's/SITENAME/superlist.johnedstone-ec2.net/g' sites/superlist.johnedstone-ec2.net/source/deploy_tools/gunicorn-upstart.template.conf  | sudo tee /etc/init/gunicorn-superlist.johnedstone-ec2.net.conf 

    sudo service nginx reload

    sudo start gunicorn-superlist.johnedstone-ec2.net 

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
