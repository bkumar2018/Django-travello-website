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
