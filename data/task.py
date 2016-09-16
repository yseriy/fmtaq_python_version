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

    def from_tuple(self, tpl):
        self.id = tpl[0]
        self.seq_id = tpl[1]
        self.queue = tpl[2]
        self.command = tpl[3]
        self.args = tpl[4]
        self.next_task_id = tpl[5]

        return self
