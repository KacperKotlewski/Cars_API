FROM python:3.8.5-buster
MAINTAINER Kacper Kotlewski

ENV PYTHONUNBUFFERED 1

RUN apt update && apt-get install -y \
    libpq-dev \
    gcc

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
COPY ./.env /app
RUN python manage.py bootup

#creating non root user for security reasons
RUN adduser -q --disabled-password user
USER user
