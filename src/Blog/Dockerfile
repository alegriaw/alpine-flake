FROM python:3.6-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /src

EXPOSE 8081

CMD cd /src && python blog.py
