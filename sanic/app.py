import os

from sanic import Sanic
from sanic.response import json
from kafka import KafkaProducer
from confluent_kafka import Producer

app = Sanic()
kafka_host = os.getenv('KAFKA_HOST').split(',')
producer = KafkaProducer(bootstrap_servers=kafka_host)

confluent_producer = Producer({'bootstrap.servers': 'kafka1'})


@app.route('/')
async def index(request):
    return json({"message": "Hello Cassie"})

@app.route('/kafka')
async def kafka_producer(request):
    producer.send('json', request.body)
    return json({"message": "Success"})

@app.route('/confluent')
async def confluent_producer(request):
    confluent_producer.produce('json', request.body)
    return json({"message": "Success"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
