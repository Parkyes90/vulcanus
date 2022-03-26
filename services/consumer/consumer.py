import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "default",
    bootstrap_servers=["kafka:9092"],
    group_id="group1",
    consumer_timeout_ms=1000,
    enable_auto_commit=True,
    auto_offset_reset="earliest",
)

print("Kafka Consumer Started!")

while True:
    consumer.poll(1)

    for message in consumer:
        print(message)
