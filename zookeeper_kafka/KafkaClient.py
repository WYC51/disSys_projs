from kafka.admin import KafkaAdminClient, NewTopic

'''
- This script is used to create a topic in Kafka cluster.
- The port number is 19092, 29092, 39092. # refer to docker-compose.yml
'''

if __name__ == "__main__":

    # Create a KafkaAdminClient object
    admin_client = KafkaAdminClient(
        bootstrap_servers=["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"], 
    )

    # Create a topic
    topic_list = []
    for topic in ["test1", "test2"]: # Add more topics if needed
        topic_list.append(NewTopic(name=topic, num_partitions=3, replication_factor=1))
    
    # Create the topic
    admin_client.create_topics(new_topics=topic_list, validate_only=False)