FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && apk update \
    && apk add py-pip \
    && apk add py3-wheel \
    && apk add py3-pymysql \
    && apk add mariadb-connector-c \
    && apk add mysql \
    && apk add mariadb-dev

RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools wheel

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt


EXPOSE 8000

ENTRYPOINT  ["python3"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


