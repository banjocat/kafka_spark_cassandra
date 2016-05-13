import random
import time

import kafka

print "Setting up producer"
PRODUCER = kafka.KafkaProducer(bootstrap_servers=['kafka:9092'])


def produce():
    votes = ('up', 'down')
    PRODUCER.send('vote', random.choice(votes))
    PRODUCER.flush()


if __name__ == "__main__":
    print "Starting produce loop"
    while True:
        produce()
        time.sleep(5)
