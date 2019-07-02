#!bin/bash
set -ex
pipenv install --deploy --system
# python promobackend/manage.py migrate
# python promobackend/manage.py runserver 0.0.0.0:8000
uwsgi --socket :8001 --module mysite.wsgi