import pika
from pika.adapters.twisted_connection import TwistedProtocolConnection
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.internet.task import LoopingCall

host = 'localhost'
port = 5672

class Worker:
    def __init__(self, queue):
        self.queue = queue

    def on_channel(self, channel):
        channel.queue_declare(queue=self.queue)
        d = channel.basic_consume(queue=self.queue)
        d.addCallback(self.on_consume)

    def on_consume(self, consume):
        queue_object, consumer_tag = consume
        loop = LoopingCall(self.queue_run, queue_object)
        loop.start(0)

    def queue_run(self, queue_object):
        d = queue_object.get()
        d.addCallback(self.on_queue_object_get)
        return d

    def on_queue_object_get(self, message):
        channel, method, properties, body = message
        print(body)
        channel.basic_ack(delivery_tag=method.delivery_tag)

def on_connect(connection):
    worker1 = Worker('hello12')
    worker2 = Worker('hello22')
    d = connection.channel()
    d.addCallback(worker1.on_channel)
    d1 = connection.channel()
    d1.addCallback(worker2.on_channel)

class FMTaQClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        parameters = pika.ConnectionParameters()
        protocol = TwistedProtocolConnection(parameters)
        protocol.add_on_open_callback(on_connect)
        return protocol

reactor.connectTCP(host, port, FMTaQClientFactory())
reactor.run()
