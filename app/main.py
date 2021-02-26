#!/usr/bin/env python
from flask import Flask,send_file,request
import socket
import struct
import glob
import random
import urllib.parse
from slideshow import slideshow_bp

app = Flask(__name__)


app.register_blueprint(slideshow_bp)

##
## Reference Functions
##
@app.route('/reference/load/<name>')
def slideshow_show(name):
    return app.send_static_file('slideshow/index.html')

##
## URL functions
##
# Not using GET for this due to a bug with parsing inputs with /'s (event it encoded in them)
# https://stackoverflow.com/questions/24519076/python-flask-url-encoded-leading-slashes-causing-404-or-405
@app.route('/url', methods=['POST'])
def open_url():
    url = request.form['url']
    url = urllib.parse.unquote(url)
    print("Got URL:", url)
    send("url|{}".format(url))
    return "ok"

## End Url Functions
