import logging
from json import dumps
from time import sleep

from kafka import KafkaProducer

from .abstract_writer import AbstractWriter

topic_name = 'sdd-lab4-topic'
logger = logging.Logger(__name__)


class KafkaWriter(AbstractWriter):
    producer = KafkaProducer(bootstrap_servers=('localhost:9092',),
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))

    @classmethod
    def write(cls, text):
        cls.producer.send(topic_name, text)
        logger.info('sent text ' + str(text[:10]) + ' to topic ' + topic_name)
