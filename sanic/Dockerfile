FROM python:3

RUN apt-get update && apt-get install -y \
        make \
        build-essential \
        libpthread-stubs0-dev \
        libssl-dev \
        libsasl2-dev \
        liblz4-dev \
        git

WORKDIR /tmp
RUN git clone https://github.com/edenhill/librdkafka
WORKDIR /tmp/librdkafka
RUN ./configure
RUN make
RUN make install


RUN pip install sanic
RUN pip install kafka-python
RUN pip install pykafka
RUN pip install confluent-kafka

RUN mkdir -p /app

WORKDIR /app
COPY . /app/.
EXPOSE 8000
# to find librdkafka libs
ENV LD_LIBRARY_PATH /usr/local/lib
CMD python3 app.py

