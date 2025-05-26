FROM python:3.13

WORKDIR /home/ajex

COPY ./project ./project/

COPY ./static ./static/

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r /home/ajex/requirements.txt



