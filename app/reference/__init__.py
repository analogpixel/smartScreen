#!/usr/bin/env python
from flask import Flask,send_file,request,Blueprint

reference_bp = Blueprint('reference', __name__, static_folder='static')

@reference_bp.route('/reference/load/<name>')
def reference_show(name):
    return reference_bp.send_static_file('index.html')


@reference_bp.route('/reference/upload')
def reference_upload():
    return ""

