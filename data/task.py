import json


class Task:

    def __init__(self):
        self.id = None
        self.seq_id = None
        self.queue = None
        self.command = None
        self.args = None
        self.next_task_id = None

    def from_string(self, string):
        task = json.loads(string)

        self.id = taks['id']
        self.seq_id = task['seq_id']
        self.queue = task['queue']
        self.command = task['command']
        self.args = task['args']
        self.next_task_id = task['next_task_id']

        return self

    def to_string(self):
        task = {
            'id'           : self.id,
            'seq_id'       : self.seq_id,
            'queue'        : self.queue,
            'command'      : self.command,
            'args'         : self.args,
            'next_task_id' : self.next_task_id,
        }

        return json.dumps(task)
