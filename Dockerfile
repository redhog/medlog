FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.8 python3-pip
RUN pip3 install flask
RUN pip3 install python-gnupg==0.4.7

ADD . /app

WORKDIR /root

CMD python3 /app/app.py
