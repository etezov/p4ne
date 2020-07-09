# Lab2.4

import json
import requests
import flask

app = flask.Flask(__name__)

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

@app.route('/')
def index():
    return flask.render_template("topology.html")

@app.route('/api/topology')
def topology():
    return flask.jsonify(response.json()['response'])


if __name__ == '__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    app.run(debug=True)
