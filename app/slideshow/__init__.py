#!/usr/bin/env python
from flask import Flask,send_file,request,Blueprint
import socket
import struct
import glob
import random
import urllib.parse


slideshow_bp = Blueprint('slideshow', __name__, static_folder='static')

def send(m):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 1122))
    client.send(m.encode('utf8'))
    from_server = client.recv(4096)
    client.close()

@slideshow_bp.route('/slideshow/activate')
def slideshow_activate():
    send("url|http://localhost:1133/slideshow/")
    return "ok"

@slideshow_bp.route('/slideshow/')
def slideshow_show():
    return slideshow_bp.send_static_file('index.html')

@slideshow_bp.route('/slideshow/random_img/')
def slideshow_random_img():
    img = random.choice( list(filter( lambda x: x.split('.')[-1].lower() in ['png','jpg','gif'] , glob.glob("slideshow/static/content/**/*", recursive=True) ) ))
    return send_file(img, mimetype='image/' + img.split('.')[-1].lower() )



