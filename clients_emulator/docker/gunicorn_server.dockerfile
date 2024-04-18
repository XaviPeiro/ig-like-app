FROM python:3.9

ENV PYTHONPATH "/app"
#ENV PATH="${PATH}:/root/.poetry/bin"
#ENV PATH /home/${USERNAME}/.local/bin:${PATH}

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && mkdir ./src

RUN poetry config virtualenvs.create false \
    && poetry install

COPY ./server_dummy ./src
ENTRYPOINT ["gunicorn", "src.server_gunicorn:app"]
CMD ["--workers=3", "-b", "0.0.0.0:9000"]


