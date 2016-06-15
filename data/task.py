import json


class Task:

    def __init__(self):
        self.task = {}

    def from_dict(self, task):
        self.task = task

    def get_body(self):
        return json.dumps(self.task)

    def get_address(self):
        return self.task['address']
