========================
django-twoscoops-project
========================

A project template for Django 1.5 based off the original twoscoops
template (https://github.com/twoscoops/django-twoscoops-project) with
built-in support for local development environments using Vagrant (http://vagrantup.com).

To use this project follow these steps:

#. Create a new virtualenv
#. Install Django
#. Create a new project using this project template
#. Run `vagrant up` to create your new local development environment
#. Run `vagrant ssh` to login
#. Change directories to /vagrant and start creating your application
#. You can login to the Django admin with the username and password 'vagrant'

*note: these instructions show creation of a project called "icecream".  You should replace this name with the actual name of your project.*

Installing Dependancies
=======================

This project template has been modified for developers using isolated virtual machines managed by Vagrant. It is still recommended that you install virtualenv on the host machine to isolate your installation of Django required to create a new project from this template.

Virtual Box
-----------

https://www.virtualbox.org/wiki/Downloads

Vagrant
-------

Vagrant (1.2+) - http://vagrantup.com/downloads

Vagrant Omnibus
---------------

vagrant-omnibus ensures the appropriate version of chef get installed.
Once you have installed vagrant, run this command::

    $ vagrant plugin install vagrant-omnibus

Vagrant Berkshelf
-----------------

Install the berkshelf gem::

    $ gem install berkshelf

vagrant-berkshelf downloads and compiles all cookbook dependancies at 
runtime so that we don't have to keep them in the project repository.
To install vagrant-berkshelf, run this command::

    $ vagrant plugin install vagrant-berkshelf

Local Virtualenv
----------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ pip install virtualenv
    $ virtualenv --distribute django

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag. You can accomplish this by
running the following command::

    $ source django/bin/activate

Installing Django
-----------------

To install Django in the new virtual environment, run the following command::

    $ pip install django

Creating your project
=====================

To create a new Django project called '**icecream**' using this project template,
run the following command::

    $ django-admin.py startproject --template=https://github.com/BNOTIONS/django-twoscoops-project/archive/develop.zip --name=Vagrantfile --extension=py,rst,html icecream

Creating your local development environment
===========================================

To create a new virtual machine running your project, run the following command::

    $ cd icecream
    $ vagrant up

Creating a new virtual machine for the first time can take several minutes.
Once completed you can login by running the following command::

    $ vagrant ssh

Once your virtual machine is up and running you can login to your project admin,
visit the following URL::

    http://localhost:8080/admin/

Login with the default username and password::

    user: vagrant
    pass: vagrant

All of the project files are all kept on your host computer and mounted inside the
virtual machine. Change directories and start coding::

    $ cd /vagrant/icecream

Adding New Requirements
=======================

Make sure that you add your pip dependancies to the correct requirements file.

Packages required only for development::

    requirements/local.txt

Packages required only for testing::

    requirements/test.txt

Packages required only for production::

    requirements/production.txt

Packages required for all enviroments::

    requiremnts/base.txt

Dev/Testing Applications
========================

Local Development
-----------------

Applications required only for local development should be added directly
to the INSTALLED_APPS list in settings/local.py configuration file like so::

    INSTALLED_APPS += (
        'django_toolbar',
    )

Testing
-------

Applications required only for testing should be added directly to the
to the INSTALLED_APPS list in settings/test.py configuration file like so::

    INSTALLED_APPS += (
        'django_jenkins',
    )

Project Applications
====================

Local Applications
-------------------

Local applications are applications you create or store locally in your project,
perhaps created by `./manage.py startapp`. Add these apps to the LOCAL_APPS list
in settings/base.py::

    LOCAL_APPS = (
        'myapp',
    )


Third Party Applications
------------------------

Third party applications are normally installed by pip and do not exist in your
project repository. Add these apps to the THIRD_PARTY_APPS list in settings/base.py::

    THIRD_PARTY_APPS = (
        'south',
    )

Django Applications
-------------------

Any applications included from Django contrib should added to the
DJANGO_APPS list in settings/base.py::

    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin panel and documentation:
        'django.contrib.admin',
        # 'django.contrib.admindocs',
   )

Acknowledgements
================

- Authors of the fantastic Twoscoops of Django book.
- Developers and contributors to the original django-twoscoops-template.
