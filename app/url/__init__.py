#!/usr/bin/env python
from flask import Flask,send_file,request,Blueprint
import requests

url_bp = Blueprint('url', __name__, static_folder='static')

def send(m):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 1122))
    client.send(m.encode('utf8'))
    from_server = client.recv(4096)
    client.close()

@url_bp.route('/url', methods=['POST'])
def open_url():
    url = request.form['url']
    url = urllib.parse.unquote(url)
    print("Got URL:", url)
    send("url|{}".format(url))
    return "ok"

