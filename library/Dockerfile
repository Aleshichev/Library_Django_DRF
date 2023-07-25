# docker build . --tag library
# docker run -p 8084:8000 library
# http://localhost:8084/

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir library
WORKDIR library

ADD requirements.txt /library/
RUN pip install -r requirements.txt

ADD . /library/

ADD .env.docker /library/.env

ENV APP_NAME=LIBRARY

RUN pip install --upgrade pip

CMD gunicorn library.wsgi:application -b 0.0.0.0:8000