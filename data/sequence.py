import json
import uuid
from data.task import Task

class Sequence:

    def __init__(self):
        self.id = None
        self.user_id = None
        self.service_type = None
        self.type = None
        self.status = None
        self.command = None
        self.args = None
        self.tasks = []

    def _id(self):
        return str(uuid.uuid4())

    def from_string(self, string):
        sequence = json.loads(string)

        self.id = self._id()
        self.user_id = sequence['user_id']
        self.service_type = sequence['service_type']
        self.type = sequence['type']
        self.status = sequence['status']
        self.command = sequence['command']
        self.args = sequence['args']

        for task_index in sequence['tasks']:
            task = Task()
            task.seq_id = self.id
            task.queue = task_index['queue']
            task.command = task_index['command']
            task.args = task_index['args']
            self.tasks.append(task)

        for task in self.tasks:
            task.id = self._id()

        for i in range(len(self.tasks) - 1):
            self.tasks[i].next_task_id = self.tasks[i + 1].id

        return self
