FROM python:3.11-slim

ARG PORT=8080

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0 \
    PORT=$PORT

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN pip install poetry && poetry install --no-root --no-directory

COPY . /code

RUN poetry install --no-dev

EXPOSE $PORT

CMD poetry run python main.py
