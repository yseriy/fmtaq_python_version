import json
from data.sequence import Sequence

s = {
#    'id'          : 'test_id',
    'type'        : 'test_type',
    'service_type': 'testsevice_type',
    'user_id'     : 'test_user_id',
    'command'     : 'test_command',
    'args'        : 'test_args',
    'tasks'       :
    [
        {
#            'seq_id'  : 'test_seq_id_1',
#            'step'    : 1,
#            'seq_size': 3,
            'address' : 'test_address1',
            'command' : 'test_command_1',
            'args'    : 'test_args_1',
        },
        {
#            'seq_id'  : 'test_seq_id_2',
#            'step'    : 2,
#            'seq_size': 3,
            'address' : 'test_address2',
            'command' : 'test_command_2',
            'args'    : 'test_args_2',
        },
        {
#            'seq_id'  : 'test_seq_id_3',
#            'step'    : 3,
#            'seq_size': 3,
            'address' : 'test_address3',
            'command' : 'test_command_3',
            'args'    : 'test_args_3',
        },
    ],
}

seq = Sequence()
seq.from_string(json.dumps(s))
task = seq.get_first_task()
print(task.get_address() + '->>' + task.get_body())
print('id: ' + seq.get_id())
s = seq.get_record()
for k in s:
    print(k + ' -> ' + s[k])
