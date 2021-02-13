#!/usr/bin/env python
from flask import Flask,send_file
import socket
import struct
import glob
import random
import urllib.parse

app = Flask(__name__)

def send(m):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 1122))
    client.send(m.encode('utf8'))
    from_server = client.recv(4096)
    client.close()


##
## Slide Show Functions
###
@app.route('/slideshow/activate')
def slideshow_activate():
    send("url|http://localhost:1133/slideshow/")
    return "ok"

@app.route('/slideshow/')
def slideshow_show():
    return app.send_static_file('slideshow/index.html')

@app.route('/slideshow/random_img/')
def slideshow_random_img():
    img = random.choice( list(filter( lambda x: x.split('.')[-1].lower() in ['png','jpg','gif'] , glob.glob("static/content/insp_pictures/**/*", recursive=True) ) ))
    return send_file(img, mimetype='image/' + img.split('.')[-1].lower() )

## End SlideShow Functions

@app.route('/url/<url>')
def open_url(url):
    url = urllib.parse.unquote(url)
    print(url)
    send("url|{}".format(url))
    return "ok"

