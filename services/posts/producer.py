from kafka import KafkaProducer
import json

producer = KafkaProducer(
    acks=0,
    compression_type="gzip",
    bootstrap_servers=["kafka:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)


def produce():
    for i in range(10):
        data = {"message": f"message {i}"}
        producer.send("default", value=data)
        producer.flush()


if __name__ == "__main__":
    produce()
