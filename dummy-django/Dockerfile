FROM --platform=linux/x86-64 python:3.9-alpine

WORKDIR /usr/src/app

ENV POETRY_HOME="/opt/poetry"
ENV VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN apk add --no-cache --virtual .build-deps build-base curl


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

EXPOSE 8000

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]