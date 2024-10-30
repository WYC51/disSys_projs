from kafka import KafkaProducer
from json import dumps
import pandas as pd

'''
- This script is used to produce data to Kafka topic.
'''

# kafka settings
TOPIC_NAME = "test1" # topic name. You can create a topic with this name in Kafka or other name you want.
BOOTSTRAP_SERVERS = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"] # port number please refer to docker-compose.yml

# create producer
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_serializer=lambda x: dumps(x).encode("utf-8")
)

# read data
df = pd.read_csv(r"data/2020-Jan_sample.csv")
dict_data = df.to_dict(orient='records')

# produce data
for i in range(len(dict_data)):
    producer.send(TOPIC_NAME, value=dict_data[i])
    producer.flush()
