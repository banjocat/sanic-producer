import os

from sanic import Sanic
from sanic.response import json
from kafka import KafkaProducer
from voluptuous import Schema, MultipleInvalid

app = Sanic()
kafka_host = os.getenv('KAFKA_HOST').split(',')
producer = KafkaProducer(bootstrap_servers=kafka_host)

schema = Schema({
    'lol': str,
    })



@app.route('/')
async def index(request):
    return json({"message": "Hello Cassie"})

@app.route('/kafka')
async def kafka_producer(request):
    try:
        schema(request.json)
        response = json({'message': 'Success'})
        producer.send('json', request.body)
    except MultipleInvalid as e:
        response = json({'message': str(e)})
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
