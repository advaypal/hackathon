#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging

import cgi, cgitb, sys, json
from scraper import *

cgitb.enable()
print "Content-type: text/json"
print
# print "Content-Type: application/html;charset=utf-8"
#
# request = json.loads(cgi.FieldStorage().value)
# print(cgi.FieldStorage().value[0].file.read())

filedata = cgi.FieldStorage().value[0]
if filedata.file:
    outfile = open("main.jpg", "w")
    outfile.write(filedata.file.read())

message = scraper(request['movieData'])

# message = json.dumps({'Status': 'Error :('})
# print(message)
