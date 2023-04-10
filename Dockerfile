FROM python:3.10-alpine3.17

LABEL authors="ahmad"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apk add --update make

RUN pip install "poetry==1.2.2"

COPY pyproject.toml poetry.lock /code/

RUN poetry config experimental.new-installer true \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


COPY . /code