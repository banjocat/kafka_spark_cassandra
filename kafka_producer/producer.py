import random
import time

import kafka


PRODUCER = kafka.KafkaProducer(bootstrap_servers=['kafka:9092'])


def produce():
    votes = ('up', 'down')
    PRODUCER.send('vote', random.choice(votes))


if __name__ == "__main__":
    while True:
        produce()
        time.sleep(5)
