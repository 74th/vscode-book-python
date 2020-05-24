FROM python:3.8
RUN apt-get update && apt-get -y install git procps
RUN pip install poetry==1.0.5

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY model ./model
COPY static ./static
COPY api.py ./

EXPOSE 8080

CMD ["poetry", "run", "python", "./api.py"]
