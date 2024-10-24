#!/bin/sh

set -e 
python manage.py collectstatic --noinput 
python manage.py migrate
uwsgi --socket :8080 --master --enable-threads --buffer-size 32768 --module myshop.wsgi 
