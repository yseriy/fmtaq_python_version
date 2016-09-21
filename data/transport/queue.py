class Queue:

    def __init__(self):
        self.queue = None
        self.declare_passive = False
        self.declare_durable = False
        self.declare_exclusive = False
        self.declare_auto_delete = False
        self.declare_arguments = None
        self.consume_no_ack = False
        self.consume_exclusive = False
        self.consume_arguments = None
        self.consume_inactivity_timeout = None

    def declare_params(self):
        return {
            'queue'      : self.queue,
            'passive'    : self.declare_passive,
            'durable'    : self.declare_durable,
            'exclusive'  : self.declare_exclusive,
            'auto_delete': self.declare_auto_delete,
            'arguments'  : self.declare_arguments,
        }

    def consume_params(self):
        return {
            'queue'             : self.queue,
            'no_ack'            : self.consume_no_ack,
            'exclusive'         : self.consume_exclusive,
            'arguments'         : self.consume_arguments,
            'inactivity_timeout': self.consume_inactivity_timeout,
        }
