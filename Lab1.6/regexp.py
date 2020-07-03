# Lab 1.6

from ipaddress import IPv4Interface
from glob import glob
from re import match


def classificator(str):
    m = match(r" ip address ((?:\d{1,3}\.){3}\d{1,3}) ((?:\d{1,3}\.){3}\d{1,3})", str)
    if m:
        return {'ip': IPv4Interface(tuple(m.group(1, 2)))}
    m = match(r"^interface (\S+)", str)
    if m:
        return {'int': m.group(1)}
    m = match(r"^hostname (\S+)", str)
    if m:
        return {'host': m.group(1)}
    return {}


dir = glob("E:\работа\Python\p4ne_training\config_files\*.txt")

iplist = []
intlist = []
hostlist = []

for i in dir:
    with open(i) as f:
        for l in f:
            line = classificator(l)
            if 'ip' in line:
                iplist.append(line['ip'])
            elif 'int' in line:
                intlist.append(line['int'])
            elif 'host' in line:
                hostlist.append(line['host'])

print('\nIP addresses:')
for i in iplist:
    print(i)

print('\nInterfaces:')
for i in intlist:
    print(i)

print('\nHostnames:')
for i in hostlist:
    print(i)
