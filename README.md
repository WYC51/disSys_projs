# Zookeeper_Kafka_Real-Time_shopping_project

This repository is designed to simulate a distributed system environment using ZooKeeper, Kafka, and Docker. It enables real-time background processing and statistical analysis of shopping order data by leveraging distributed data storage and processing across multiple nodes. ZooKeeper is utilized for coordinating and managing distributed system states, Kafka serves as the messaging platform for high-throughput, low-latency data streaming, and Docker ensures an isolated and scalable environment for deploying the system components. This setup effectively demonstrates the integration of these technologies to achieve fault-tolerance, scalability, and real-time insights in a distributed architecture.

__This repository is a collaborative group project for a course.__

- Environment
  - Docker
  - Linux 

- Dependencies:
    - `pip install -r requirements.txt`
    
- Docker Env :
    - `docker-compose up -d --remove-orphans`

- Create topic
    - `python KafkaClient.py`
    - Run this code when first run the repo

- Consumner
  - `python KafkaConsumer.py`

- Producer
  - `pytohn Producer.py`

- References
  - Data source: https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
  - For more details, please refer to our [presentation](./zookeeper_kafka/pdf/分散式系統期末報告%20Kafka%20應用.pdf)
