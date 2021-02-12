#!/usr/bin/env python

import socket
from selenium import webdriver

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get("http://www.google.com")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 1122))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode('utf8')
        print(from_client)
        conn.send("I am SERVER<br>".encode('utf8'))
    conn.close()
    [cmd,data] = from_client.split('|')
    print(cmd,data)
    if cmd == 'url':
        browser.get(data)
        
    print('client disconnected')
