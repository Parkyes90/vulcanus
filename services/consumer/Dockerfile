FROM python:3.10-alpine

# env
ENV USER=consumer \
    HOME=/home/consumer
ENV USER_BIN_PATH=${HOME}/.local/bin
ENV PATH $PATH:${USER_BIN_PATH}

RUN apk add build-base libffi-dev

# group
RUN addgroup $USER

# user
RUN adduser \
    --disabled-password \
    --home "$HOME" \
	--ingroup "$USER" \
    "$USER"

USER consumer
WORKDIR $HOME/app

## python deps
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv

COPY Pipfile* $HOME/app/
ENV PYTHONUNBUFFERED 1

RUN pipenv sync

COPY . $HOME/app