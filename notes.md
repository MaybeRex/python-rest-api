# DJANGO REST API TUTORIAL NOTES

## Vagrant

* To initialize a vagrant file simply do `vagrant init`
* vagrant automatically syncs up working directory and the `/vagrant` folder in the vagrant vm

## VirtualEnv

*  On Ubuntu + Vagrant `16.05 LTS`
    * to create a python virtual env `mkvirtualenv profiles_api --python=python3` with `virtualenvwrapper` installed
    *  to exit a VirtualEnv `deactivate`
    * to re enter `workon profiles_api` or your custom name

## DJANGO

* To create a `django` project, simply navigate to the target dir and enter

```shell
django-admin.py startproject PROJECTNAME
```

* After that project has been made, you can create more projects using the `manage.py` file and using it in a similar way

```shell
python3 manage.py startapp SECONDPROJECT
```

* After the project has been created, `PROJECTNAME/PROJECTNAME/settings.py` file is the file that will have all the setting for the django project
    * Here inside the `INSTALLED_APPS` array you can add libraries, such as `rest_framework`, `rest_framework.authtoken`, or your custom app, in this case `profiles_api`

### Django Development Server
* to run `python3 manage.py runserver 0.0.0.0:8080`

### Models

* Models describe the data that we need for our application
* Django uses these models to map our data to our db
    * Pretty much has a built in ORM
    * They have a lot of abstract classes and its easy to get setup
* `admin.py` is where you register your models
    * This is to use the admin site that django makes for you, if you don't want it then just don't use it


### Django REST framework views
* APIView
    * Most Basic type of view
    * Uses HTTP methods
* Viewset
    * Accept functions that map to common API object actions
        * EX
            * List
            * Create
            * Retrieve
            * Update
            * Partial Update
            * Destroy
    * Only use if you need quick and simple CRUD interface
    * If you are working with a standard data structure
    * Lets one use the `Routers` class in the Django REST framework   

### Django REST framework Serializer
* It is an object that we can use to describe the data that needs to return and retrieve from our APIView
* Converts text JSON to python object and vice-versa

### Django urls
* Availalbe in the `urls.py` file for custom URLs to be added or deleted

### Migrations
* To use our user model, we need to add it to our `settings.py` by adding `AUTH_USER_MODEL = 'DJANGO_APP.USER_CLASS'`(caps are for your custom name)
* Then migrations have to be made, run ` python3 manage.py makemigrations` to make the migration file and establish the db script
    * To run the script(s) created, run `python3 manage.py migrate`

## requirements.txt

* same thing as package.json but for python
* `pip freeze` to see all the currently installed packages

## postgresql

* username `msolorzano` password `rexrexRex+3`
* database name `electronStore`

## Open a DB w/ user privileges

* to start a db session `sudo -u postgres psql`

### Creating a DB

```shell
CREATE DATABASE electronstore;
```

### Create a User for managing the db and to connect to w/ django

```shell
CREATE USER msolorzano WITH PASSWORD 'rexrexRex+3';
```

### Initial Postgres setup

```shell
ALTER ROLE msolorzano SET client_encoding TO 'utf8';
ALTER ROLE msolorzano SET default_transaction_isolation TO 'read committed';
ALTER ROLE msolorzano SET timezone TO 'UTC';
```

### Give user permissions

```shell
GRANT ALL PRIVILEGES ON DATABASE electronstore TO msolorzano;
```
