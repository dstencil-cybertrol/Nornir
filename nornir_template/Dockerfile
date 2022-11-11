# syntax=docker/dockerfile:1


FROM python:3.11-rc-alpine

WORKDIR /nornir
COPY . /nornir
RUN pip install -U pip && \
    pip install -U setuptools && \
    apk --update add bash && \
    apk add libxml2-dev libxslt-dev g++ postgresql-dev cargo gcc python3-dev libffi-dev musl-dev zlib-dev jpeg-dev git && \
    pip install pandas && \
	pip install -r requirements.txt && \
	git clone https://github.com/dstencil/Nornir.git
COPY requirements.txt requirements.txt
