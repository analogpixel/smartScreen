#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get("http://www.google.com")

