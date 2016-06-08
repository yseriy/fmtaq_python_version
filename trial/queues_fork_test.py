import os
import time
import pika

parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(parameters)

def callback(ch, method, properties, body):
    print(" [x] Received hello11 %r" % body)

newpid = os.fork()

if newpid == 0:
    channel = connection.channel(channel_number=1)
    channel.queue_declare(queue='hello11')
    channel.basic_consume(callback, queue='hello11', no_ack=True)
else:
    channel = connection.channel(channel_number=2)
    channel.queue_declare(queue='hello12')
    channel.basic_consume(callback, queue='hello12', no_ack=True)
