import uuid
import psycopg2

dsn = r'dbname=fmtaq user=yseriy host=localhost'
sql = "INSERT INTO sequence VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\')"
tasks = ('[{{"arg": "test_args_1", "step": 1, "seq_id": "{0}", '
         '"command": "test_command_1", "seq_size": 3}}, '
         '{{"args": "test_args_2", "step": 2, "seq_id": "{0}", '
         '"command": "test_command_2", "seq_size": 3}}, '
         '{{"args": "test_args_3", "step": 3, "seq_id": "{0}", '
         '"command": "test_command_3", "seq_size": 3}}]')

connect = psycopg2.connect(dsn)
cursor = connect.cursor()

for i in range(1):
    u = str(uuid.uuid1())
    t = tasks.format(u)
#    cursor.execute(sql.format(
    print(sql.format(
        u,
        'chain',
        'unixfm',
        'test_user_' + str(i),
        'test_command_' + str(i),
        'test_args_' + str(i),
        'running', t))

#connect.commit()
cursor.close()
connect.close()
