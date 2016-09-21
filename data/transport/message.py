class Message:

    def __init__(self):
        self.reply_to = None
        self.correlation_id = None
        self.body = None
        self.publish_exchange = None
        self.publish_routing_key = None
        self.publish_properties = None
        self.publish_mandatory = False
        self.publish_immediate = False

    def from_list(self, raw_message):
        self.reply_to = raw_message[1].reply_to
        self.correlation_id = raw_message[1].correlation_id
        self.body = raw_message[2]

    def properties(self):
        return {
            'reply_to'       : self.reply_to,
            'correlation_id' : self.correlation_id,
        }

    def publish_params(self):
        return {
            'exchange'    : self.publish_exchange,
            'routing_key' : self.publish_routing_key,
            'body'        : self.body,
            'properties'  : self.publish_properties,
            'mandatory'   : self.publish_mandatory,
            'immediate'   : self.publish_immediate,
        }
