from json import loads

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sdd-lab4-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))


for msg in consumer:
    print(msg)
