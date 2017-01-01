FROM python:3

RUN pip install sanic
RUN pip install kafka-python

RUN mkdir -p /app

WORKDIR /app
COPY . /app/.
EXPOSE 8000
CMD python3 app.py

