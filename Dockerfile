FROM python:3.10-slim AS base

ENV POETRY_HOME=/opt/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get install libprotobuf-dev protobuf-compiler -y \
  && apt-get install cmake -y 

RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

FROM base AS builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-interaction

FROM base AS runner

WORKDIR /app
COPY --from=builder /app/.venv/ /app/.venv/

COPY . /app
RUN mkdir -p /db

EXPOSE 8000

FROM runner AS development

WORKDIR /app

