FROM python:3.7
RUN apt-get update && apt-get -y install git procps

WORKDIR /app
ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./dev-requirements.txt ./
RUN pip install -r dev-requirements.txt
