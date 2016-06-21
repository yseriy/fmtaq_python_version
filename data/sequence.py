import json
import uuid
from data.task import Task


class Sequence:

    def __init__(self):
        self.sequence = {}

    def from_string(self, string):
        self.sequence = json.loads(string)
        self.sequence['id'] = str(uuid.uuid1())
        sequence_size = len(self.sequence['tasks'])

        step = 0
        for task in self.sequence['tasks']:
            task['seq_id'] = self.sequence['id']
            task['step'] = step + 1
            task['seq_size'] = sequence_size

    def get_id(self):
        return self.sequence['id']

    def get_type(self):
        return self.sequence['type']

    def get_first_task(self):
        task = Task()
        task.from_dict(self.sequence['tasks'][0])
        return task

    def get_record(self):
        s = self.sequence.copy()
        s['tasks'] = json.dumps(s['tasks'])
        return s
