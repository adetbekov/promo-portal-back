# FROM python:3
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1
# RUN mkdir /promo-portal-back
# WORKDIR /promo-portal-back
# RUN pip install pipenv==2018.10.13
# ADD Pipfile /promo-portal-back/
# ADD Pipfile.lock /promo-portal-back/
# RUN set -ex && pipenv install --deploy --system
# RUN pip install django-cities-light
# ADD . /promo-portal-back/
FROM python:3
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
RUN pip install pipenv==2018.10.13
RUN set -ex && pipenv install --deploy --system
RUN pip install django-cities-light
RUN pip install uwsgi
RUN pip install psycopg2
# docker-compose execの開始位置
WORKDIR /app/promobackend/