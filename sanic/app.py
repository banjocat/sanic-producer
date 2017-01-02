import os

from sanic import Sanic
from sanic.response import json
from kafka import KafkaProducer

app = Sanic()
kafka_host = os.getenv('KAFKA_HOST').split(',')
producer = KafkaProducer(bootstrap_servers=kafka_host)

@app.route('/')
async def index(request):
    return json({"message": "Hello Cassie"})

@app.route('/kafka')
async def kafka_producer(request):
    await producer.send('json', request.body)
    return json({"message": "Success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
