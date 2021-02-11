#!/usr/bin/env python
from selenium import webdriver
from flask import Flask

app = Flask(__name__)

browser = webdriver.Firefox()
browser.fullscreen_window()

@app.route('/')
def hello_world():
    global browser
    browser.get("http://www.google.com")
    return app.send_static_file('index.html')

