# Django-travello-website

This is sample website using Travello free templates project name [HelloWorld]

Technologies used :  pip freeze : ===> 
asgiref==3.2.3
Django==2.1.15
django-pyodbc==1.1.3
django-pyodbc-azure==2.1.0.0
Pillow==7.0.0
pyodbc==4.0.30
pytz==2019.3
sqlparse==0.3.0

Database:
MSSQL server 2014

///////////////////////////////////

git clone https://github.com/bkumar2018/Django-travello-website.git
pip list # check for all the require modules present if not then install as below:
pip install django
pip install Pillow
Edit settings.py as per DB configurations

#python manage.py makemigrations
Migrations for 'travello':
  travello\migrations\0001_initial.py
    - Create model Destination
#python manage.py sqlmigrate travello 0001	
#python manage.py migrate

#python manage.py createsuperuser 

/////
DB configuration for MySQL DB :
# Database settings for MySQL in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',        
        'NAME': 'travello',
        'USER': 'dbadmin',
        'PASSWORD': '******',
        'HOST': 'localhost', 
        'PORT': 3306,
    }
}
////

Download mysqlclient file "mysqlclient-1.4.6-cp38-cp38-win32.whl" from link : "https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient" 
Run command to install it.
#pip install mysqlclient-1.4.6-cp38-cp38-win32.whl

OPen Mysql WorkBench.
create database travello; 
create user dbadmin identified by '******';   --- This is fine if Mysql version is below 8.0
grant all on travello.* to 'dbadmin'@'%';
flush privileges;

show variables like '%version%';    --- Check the mysql db version 8.0.9

-- For ERROR : django.db.utils.OperationalError: (2059, "Authentication plugin 'caching_sha2_password' cannot be loaded: The specified module could not be found.\r\n") 
-- Solution:  CREATE USER 'username'@'ip_address' IDENTIFIED WITH mysql_native_password BY 'password';
OR
-- ALTER USER 'dbadmin'@'%' IDENTIFIED WITH mysql_native_password BY '******';


