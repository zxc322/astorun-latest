FROM python:3.8-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/astorun_2022

WORKDIR /usr/src/astorun_2022 
EXPOSE 8000

RUN pip install --upgrade pip
COPY ./req.txt /usr/src/astorun_2022/req.txt
RUN pip install -r /usr/src/astorun_2022/req.txt
COPY . /usr/src/astorun_2022


