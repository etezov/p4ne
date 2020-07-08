# Lab2.1

import paramiko
import time
import re
import pprint

BUF_SIZE = 20000
TIMEOUT = 1

ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_conn.connect('10.31.72.160', username='restapi', password='j0sg1280-7@', look_for_keys=False, allow_agent=False)


session = ssh_conn.invoke_shell()

session.send('\n')
session.send('terminal length 0\n')
time.sleep(TIMEOUT)

session.send('\n')
session.send('show interface\n')
time.sleep(TIMEOUT*2)
out = session.recv(BUF_SIZE)
out_dec = out.decode()

session.close()


exp = re.finditer(r'(\S+) is .+?, line protocol is.+?(\d+) packets input, (\d+) bytes.+?(\d+) packets output, (\d+) bytes', out_dec, re.S)
result = {}
for i in exp:
    ifs = i.group(1)
    input_packets = i.group(2)
    input_bytes = i.group(3)
    output_packets = i.group(4)
    output_bytes = i.group(5)
    result[ifs] = {'input_packets': input_packets,
                   'input_bytes': input_bytes,
                   'output_packets': output_packets,
                   'output_bytes': output_bytes}

pprint.pprint(result)



