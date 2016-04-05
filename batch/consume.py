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

while True:
        """
        consume the kafka queue
        """
        consumer = KafkaConsumer('new-ride-topic', group_id='ride-indexer', bootstrap_servers=['kafka:9092'])
        for message in consumer:
            new_ride = json.loads((message.value).decode('utf-8'))
            create_new_ride(new_ride)
        
        # todo: handle other topics (queues)



def create_new_ride(new_ride):
    es = Elasticsearch(['es'])
    es.index(
        'ride_index',
        doc_type='ride',
        id=new_ride['ride_id'],
        body=new_ride
    )
    es.indices.refresh(index="ride_index")
