FROM python:3.10-slim as builder
WORKDIR /server

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile* ./

RUN pipenv install --system --ignore-pipfile

COPY . ./

EXPOSE 8000

FROM builder as development
RUN pipenv install --system --dev --ignore-pipfile

FROM builder as production
CMD gunicorn config.wsgi:application -b 0.0.0.0:8000 --log-level info --access-logfile - --error-logfile -
