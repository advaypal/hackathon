#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging

# import cgi, cgitb, sys, json
from scraper import *
from image_handler import *

# cgitb.enable()
# print "Content-type: text/json"
# print
# print "Content-Type: application/html;charset=utf-8"
#
# request = json.loads(cgi.FieldStorage().value)
# print(cgi.FieldStorage().value[0].file.read())


# take input form main page
# filedata = cgi.FieldStorage().value[0]
def write_img(fileData):

    # outfile = open("static/img/main.jpg", "w")
    # filedata.save(outfile)

    # movieData = image_search("https://fathomless-lake-87854.herokuapp.com/img")
    ###
	movieDatadict = finalScraper(fileData) #finalScraper(movieData)
	jsonData = json.dumps(movieDatadict)
	return jsonData
