import pika


class RabbitMQ:

    def __init__(self):
        self.parameters = pika.ConnectionParameters()
        self.message = Message()
        self.listen_queue = Queue()
        self.route_queue = Queue()

    def connect(self):
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(**self.listen_queue.declare_params())

    def disconnect(self):
        self.channel.close()
        self.connection.close()

    def reconnect(self):
        if self.connection.is_closed(): self.connect()

    def receive_sequence(self):
        message = self.channel.consume(**self.listen_queue.consume_params())
        self.channel.cancel()
        self.message.from_list(message)
        return self.message.body()
