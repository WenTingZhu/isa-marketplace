import time
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch

# these are the things that a user will likely use to search for a ride
# new_ride = {
#     'ride_id':ride_id,
#     'open_seats':open_seats,
#     'departure': departure,
#     'status':status,
#     'dropoffLocation_name': dropoffLocation_name,
#     'dropOffLocation_address':dropOffLocation_address,
#     'dropOffLocation_city':dropOffLocation_city,
#     'dropOffLocation_state':dropOffLocation_state,
#     'dropOffLocation_zipcode': dropOffLocation_zipcode,
# }
CREATE = 'create-ride-topic'
UPDATE = 'update-ride-topic'
DELETE = 'delete-ride-topic'

def create_new_ride(new_ride):
    es = Elasticsearch(['es'])
    es.index(
        'ride_index',
        doc_type='ride',
        id=new_ride['ride_id'],
        body=new_ride
    )
    # es.indices.refresh(index="ride_index")

def update_ride(ride):
    es = Elasticsearch(['es'])
    es.index(
        'ride_index',
        doc_type='ride',
        id=ride['ride_id'],
        body=ride
    )
def delete_ride(ride):
    es = Elasticsearch(['es'])
    es.delete(
        index='ride_index',
        doc_type='ride',
        id=new_ride['ride_id'],
    )

topics = {
    CREATE: create_new_ride,
    UPDATE: update_ride,
    DELETE: delete_ride,
}

# sleep to make sure kafka is running
# time.sleep(30)
# producer = KafkaProducer(bootstrap_servers='kafka:9092')
# if type == CREATE:
#     kafka_queue = 'create-ride-topic'
# elif type == UPDATE:
#     kafka_queue = 'update-ride-topic'
# else:
#     kafka_queue = 'delete-ride-topic'
# raise "adding to kafka queue"
# producer.send(kafka_queue, json.dumps(job).encode('utf-8'))
while True:
        """
        consume the kafka queue
        """
        for consumer_name in topics.keys():
            # KafkaConsumer().ensure_topic_exists(consumer_name, bootstrap_servers=['kafka:9092'])
            consumer = KafkaConsumer(
                consumer_name,
                group_id='ride-indexer',
                bootstrap_servers=['kafka:9092']
            )
            consume.ensure_topic_exists(consumer_name)
            for message in consumer:
                job = json.loads((message.value).decode('utf-8'))
                topics[consumer_name](job)
