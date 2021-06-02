FROM python:3.9-slim-buster

ENV MICRO_SERVICE=/lemonster-api
ENV U=lemonster-api
# set work directory

RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install libmagic1 -y

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $MICRO_SERVICE

RUN pip install --upgrade pip
RUN pip install -r requirements.txt gunicorn

CMD ["/bin/bash"]
