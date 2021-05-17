FROM python:3.9-alpine

ENV MICRO_SERVICE=/home/jsyme/lemonster-api
RUN addgroup -S lemonster-api && adduser -S lemonster-api -G lemonster-api
# set work directory


RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev gcc \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $MICRO_SERVICE
RUN pip install -r requirements.txt gunicorn
COPY ./docker-entrypoint.sh $MICRO_SERVICE

CMD ["echo "running"]
