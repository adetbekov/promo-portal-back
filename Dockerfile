FROM python:3
RUN mkdir /promo-portal-back
WORKDIR /promo-portal-back
RUN pip install pipenv
COPY Pipfile ./
COPY Pipfile.lock ./
RUN set -ex && pipenv install --deploy --system
COPY . .
