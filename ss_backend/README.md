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
for each app
python manage.py makemigrations <appname> 
python3 manage.py migrate


## Simple migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Reset the DB so that it contains no data and migrations can be run again
$ ./manage.py reset_db mybucket

# Don't ask for a confirmation before doing the reset
$ ./manage.py reset_db --noinput