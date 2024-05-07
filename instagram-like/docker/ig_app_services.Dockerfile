FROM python:3.10
LABEL authors="ras"

ENV PYTHONPATH "/app"

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && mkdir ./src

RUN poetry config virtualenvs.create false \
    && poetry install

RUN mkdir -p /docker/entrypoints
COPY docker/init-ig-like-w-migrations.sh /docker/entrypoint.sh
RUN chmod +x /docker/entrypoint.sh

COPY ./instagram_like ./src

WORKDIR /app/src

#ENTRYPOINT ["uvicorn"]
#CMD ["src.entrypoint:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]