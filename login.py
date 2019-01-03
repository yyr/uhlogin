#!/usr/bin/env python

# University of Hyderabad's Captive portal login with webdriver.
import sys, time
from selenium import webdriver

driver = webdriver.Firefox()

try:
	driver.get("https://192.168.56.2:8090/httpclient.html")
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("USERNAME")  # replace
password.send_keys("PASSWORD")  # replace

driver.find_element_by_id("loginbutton").click()
# time.sleep(5)
print "Logged In."
driver.close()
