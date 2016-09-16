import json


class Result:

    def __init__(self):
        self.task_id = None
        self.seq_id = None
        self.return_code = None
        self.return_value = None
        self.error_text = None

    def from_string(self, string):
        result = json.loads(string)

        self.task_id = result['task_id']
        self.seq_id = result['seq_id']
        self.return_code = result['return_code']

        if 'return_value' in result:
            self.return_value = result['return_value']

        if 'error_text' in result:
            self.error_text = result['error_text']

        return self
