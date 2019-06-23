FROM python:3.7
WORKDIR /app
COPY ./requirementes.txt ./
RUN pip install -r requirementes.txt
COPY model ./
COPY static ./
COPY api.py ./

EXPOSE 5000
