#!/usr/bin/env python
from flask import Flask
import socket
import struct

app = Flask(__name__)

def send(m):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 1122))
    client.send(m.encode('utf8'))
    from_server = client.recv(4096)
    client.close()

@app.route('/url/<prefix>/<postfix>')
def open_url(prefix,postfix):
    print(prefix,postfix)
    send("url|{}://{}".format(prefix,postfix))
    return "ok"

