import time
from kafka import KafkaConsumer

while True:
    time.sleep(30)
    print('haha consuming something in the kafka queue')


# def consume_kafka_queue():
#     this function belongs inside the kafka container. NOT IN THIS FILE.
#     while True:
#         consumer = KafkaConsumer('new-ride-topic', group_id='ride-indexer', bootstrap_servers=['kafka:9092'])
#         for message in consumer:
#             new_ride_
