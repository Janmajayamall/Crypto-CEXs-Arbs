import pika
import sys
from time import sleep

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.exchange_declare(exchange="quote_updates", exchange_type="fanout")

for i in range(1000):
    sleep(1)
    channel.basic_publish(exchange="quote_updates", routing_key="", body=str(i))
    print("sent", i)

connection.close()


