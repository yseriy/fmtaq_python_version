import pika


class RabbitMQ:

    def __init__(self):
        self.connection_params = None
        self.listen_queue = None
        self.result_queue = None
        self.routing_queue = None
        self.sequence = None
        self.result = None
        self.seq_message = None
        self.result_message = None
        self.task_message = None

        self.connection = None
        self.channel = None

    def connect(self):
        connection_params = self.connection_params.get_params()
        connection_params['credentials'] = pika.PlainCredentials(
            **self.connection_params.credentials()
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(**connection_params)
        )
        self.channel = self.connection.channel()

    def disconnect(self):
        self.channel.close()
        self.connection.close()

    def reconnect(self):
        if self.connection.is_closed():
            self.connect()

    def receive_sequence(self):
        declare_params = self.listen_queue.declare_params()
        consume_params = self.listen_queue.consume_params()

        self.channel.queue_declare(**declare_params)
        for raw_message in self.channel.consume(**consume_params):
            self.seq_message.from_list(raw_message)
            break
        self.channel.cancel()
        self.sequence.from_string(self.seq_message.body.decode("utf-8"))

        return self.sequence

    def send_sequence_id(self, sequence_id):
        self.seq_message.publish_routing_key = self.seq_message.reply_to
        self.seq_message.body = sequence_id

        publish_params = self.seq_message.publish_params()
        publish_params['properties'] = pika.BasicProperties(
            **self.seq_message.properties()
        )
        self.channel.publish(**publish_params)

    def send_task(self, task):
        self.routing_queue.queue = task.queue
        self.channel.queue_declare(**self.routing_queue.declare_params())

        self.task_message.publish_routing_key = task.queue
        self.task_message.body = task.to_string()
        self.channel.publish(**self.task_message.publish_params())

    def receive_result(self):
        declare_params = self.result_queue.declare_params()
        consume_params = self.result_queue.consume_params()

        self.channel.queue_declare(**declare_params)
        for raw_message in self.channel.consume(**consume_params):
            self.result_message.from_list(raw_message)
            break
        self.channel.cancel()

        return self.result.from_string(self.result_message.body.decode("utf-8"))
