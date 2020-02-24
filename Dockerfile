FROM python:3.8-alpine

MAINTAINER Niraj Khatiwada

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /dockerapp
WORKDIR /dockerapp
COPY ./app /dockerapp

RUN adduser -D niraj
USER niraj
