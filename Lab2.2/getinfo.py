# Lab 2.2

from flask import Flask
from flask import jsonify
from glob import glob
from re import match
from ipaddress import IPv4Interface

app = Flask(__name__)
hostlist = []
ipdict = {}


@app.route('/')
def index():
    return "Для получения списка хостов перейдите в раздел \"/configs\"" \
           "<br>Для получения сведений об IP-адресах конкретного хоста перейдите в раздел \"/config/<i>&lt;hostname&gt;</i>\""


@app.route('/configs')
def configs():
    return jsonify('Hostnames:', hostlist)


@app.route('/configs/<path:hostname>')
def byhostname(hostname):
    return jsonify('Host <%s> IP int brief' % hostname, ipdict[hostname])


if __name__ == '__main__':
    dir = glob("E:\работа\Python\p4ne_training\config_files\*.txt")
    for i in dir:
        with open(i) as f:
            iplist = []
            intlist = []
            ipint = {}
            for l in f:
                m = match(r"hostname (\S+)", l)
                if m:
                    host = str(m.group(1))
                    hostlist.append(host)
                m = match(r"interface (\S+)", l)
                if m:
                    iface = str(m.group(1))
                    intlist.append(iface)
                m = match(r" ip address ((?:\d{1,3}\.){3}\d{1,3}) ((?:\d{1,3}\.){3}\d{1,3})", l)
                if m:
                    ip = IPv4Interface(tuple(m.group(1, 2)))
                    iplist.append(ip)
                    ipint[iface] = ip.with_prefixlen
            ipdict[host] = ipint

    app.run(debug=True)
