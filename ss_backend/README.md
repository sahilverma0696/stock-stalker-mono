# stock-stalker

## Run server
python3 manage.py runserver;    

## CRON 
python3 manage.py crontab add;
python3 manage.py crontab show;
python3 manage.py crontab remove;

## Migrations 

## Reset migrations
In case you decide to delete all migrations and delete all db 
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete;
find . -path "*/migrations/*.pyc"  -delete;
rm db.sqlite3;
for each app
python manage.py makemigrations <appname> 
python3 manage.py migrate


## Simple migrations
python3 manage.py makemigrations
python3 manage.py migrate
