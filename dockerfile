FROM python:3.11.2-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /tour_house_management

COPY requirements.txt /tour_house_management/

RUN  pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /tour_house_management/