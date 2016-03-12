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
request = json.loads(cgi.FieldStorage().value)

message = scraper(request['movieData'])

# message = json.dumps({'Status': 'Error :('})
print(message)

db.close()
