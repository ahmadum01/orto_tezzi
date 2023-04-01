FROM python:3.10-alpine

LABEL authors="ahmad"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code