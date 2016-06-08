import pika

channel = None

def on_connected(connectin):
    connection.channel(on_channel_open)

def on_channel_open(new_channel):
    global channel
    channel = new_channel
    channel.queue_declare(queue="hello", durable=False, exclusive=False,
                          auto_delete=True, callback=on_queue_declared)
    channel.queue_declare(queue="hello1", durable=False, exclusive=False,
                          auto_delete=True, callback=on_queue_declared1)

def on_queue_declared(frame):
    channel.basic_consume(handle_delivery, queue='hello')

def on_queue_declared1(frame):
    channel.basic_consume(handle_delivery1, queue='hello1')

def handle_delivery(channel, method, header, body):
    print("P1")
    print(method)
    print(header)
    print(body)

def handle_delivery1(channel, method, header, body):
    print("P2")
    print(method)
    print(header)
    print(body)

parameters = pika.ConnectionParameters()
connection = pika.SelectConnection(parameters, on_connected)

try:
    connection.ioloop.start()
except KeyboardInterrupt:
    connection.close()
    connection.ioloop.start()
