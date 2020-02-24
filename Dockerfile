FROM python:3.8-alpine

MAINTAINER Niraj Khatiwada

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /dockerapp
WORKDIR /dockerapp
COPY ./app /dockerapp

RUN adduser -D niraj
USER niraj
