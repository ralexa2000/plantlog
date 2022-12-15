FROM python:3.9-buster

RUN mkdir app
WORKDIR /app

RUN pip install "poetry==1.3.1"
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY src/ .
