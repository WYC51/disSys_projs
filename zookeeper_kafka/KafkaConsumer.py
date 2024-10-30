from kafka import KafkaConsumer
from json import loads
import matplotlib.pyplot as plt



'''
- This script is a Kafka consumer that reads the data from the Kafka topic and updates the bar chart based on the price ranges.
'''

# Kafka setting
TOPIC_NAME = "test1" # Topic name
BOOTSTRAP_SERVERS = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:39092"] # refer to the docker-compose.yml

# Kafka consumer    
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: loads(x.decode("utf-8"))
)

# Column names from CSV file
event_types = ['view', 'cart', 'remove_from_cart', 'purchase']

# Initialize the price ranges and the figure
price_ranges = {
    "0-10": {event_type: 0 for event_type in event_types},
    "10-20": {event_type: 0 for event_type in event_types},
    "20-30": {event_type: 0 for event_type in event_types},
    "30-40": {event_type: 0 for event_type in event_types},
    "40-50": {event_type: 0 for event_type in event_types},
    ">50": {event_type: 0 for event_type in event_types}
}

# Initialize the figure
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
fig.tight_layout(pad=3.5)

# Set the title and labels
titles = ["View", "Cart", "Remove from Cart", "Purchase"]
x_label = "Price Range"
y_label = "Transaction Count"

# Create the bar chart
bars = []
for i, ax in enumerate(axes.flatten()):
    ax.set_title(titles[i])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    bar = ax.bar(price_ranges.keys(), [0] * len(price_ranges), tick_label=list(price_ranges.keys()))
    bars.append(bar)

def update_graph():
    # Update the bar chart
    for j, bar in enumerate(bars):
        for k, rect in enumerate(bar):
            price_range = list(price_ranges.keys())[k]
            rect.set_height(price_ranges[price_range][event_types[j]])

    max_count = max([price_ranges[key][event_type] for key in price_ranges for event_type in event_types])
    for ax in axes.flatten():
        ax.set_ylim(0, max_count + 1)

    plt.draw()

# Start the consumer
for msg in consumer:
    event_type = msg.value["event_type"]
    price = msg.value["price"]

    # Update the price ranges based on the price_ranges
    if 0 <= price < 10:
        price_ranges["0-10"][event_type] += 1
    elif 10 <= price < 20:
        price_ranges["10-20"][event_type] += 1
    elif 20 <= price < 30:
        price_ranges["20-30"][event_type] += 1
    elif 30 <= price < 40:
        price_ranges["30-40"][event_type] += 1
    elif 40 <= price < 50:
        price_ranges["40-50"][event_type] += 1
    elif price > 50:
        price_ranges[">50"][event_type] += 1

    update_graph() # Update the graph
    plt.pause(0.01)
