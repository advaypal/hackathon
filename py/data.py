#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging

# import cgi, cgitb, sys, json
from scraper import *
# from image_handler import *

# cgitb.enable()
# print "Content-type: text/json"
# print
# print "Content-Type: application/html;charset=utf-8"
#
# request = json.loads(cgi.FieldStorage().value)
# print(cgi.FieldStorage().value[0].file.read())


# take input form main page
# filedata = cgi.FieldStorage().value[0]
def write_img(filedata):
    if filedata.file:
        outfile = open("../static/img/main.jpg", "w")
        outfile.write(filedata.file.read())

    movieData = get_guess()

    movieDatadict = finalScraper(movieData)
    jsonData = json.dumps(movieDatadict)
    return jsonData

#image manipulation function which returns movieData

#convet this dict to json and send to angular



# message = json.dumps({'Status': 'Error :('})
# print(message)
