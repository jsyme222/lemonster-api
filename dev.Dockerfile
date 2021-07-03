FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt update && apt install libmagic-dev -y
RUN pip install -r requirements.txt
COPY . /code/
