FROM python:3.10-alpine

LABEL authors="ahmad"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install "poetry==1.2.2"

COPY pyproject.toml poetry.lock /code/

RUN apt-get update \
    && apt-get install make \
    && rm -rf /var/lib/apt/lists/*

RUN poetry config experimental.new-installer true \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


COPY . /code