# ZookeeperClient
This repo uses ZooKeeper, Kafka, and Docker to simulates a distributed system environment, enabling real-time background statistics on shopping orders by leveraging data storage and processing across multiple nodes.

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
  - For more details, please refer to our [presentation](./pdf/分散式系統期末報告%20Kafka%20應用.pdf)