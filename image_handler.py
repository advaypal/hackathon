#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
# enable debugging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
from splinter import Browser

def image_crop():
    main = Image.open("main.jpg")
    size = main.size()
    main.crop(0, 0, size[0], 3 * size[1] / 4).save("crop1.jpg")
    main.crop(0, size[1] / 4, size[0], size[1]).save("crop2.jpg")
    main.crop(size[0] / 4, 0, size[0], size[1]).save("crop1.jpg")
    main.crop(0, 0, 3 * size[0] / 4, size[1]).save("crop1.jpg")

def image_search(image_url):
    # driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    # driver.set_window_size(1280, 1024)
    # driver.get("https://www.google.com/searchbyimage?&image_url=" + image_url)
    # driver.save_screenshot('image.jpg')
    # print('_gUb' in driver.page_source)
    # guess = driver.find_element_by_class_name("_gUb").text
    # driver.close()
    # return guess
    browser = Browser('chrome')
    browser.visit("https://www.google.com/searchbyimage?&image_url=" + image_url)
    print('_gUb' in browser.html)
    guess = browser.find_by_css('._gUb').value
    print(guess)

def get_guess():
    image_crop()
    guesses = [image_search("https://fathomless-lake-87854.herokuapp.com/img/"),
               image_search("crop1.jpg"),
               image_search("crop2.jpg"),
               image_search("crop3.jpg"),
               image_search("crop4.jpg")
               ]
    counts = [guesses.count(guess) for guess in guesses]
    return guesses[count.index(max(count))]
    return image_search("")

image_search("http://assets.flicks.co.nz/images/movies/poster/49/494ba9ff03bdad881378a6fd4092a6c7_500x735.jpg")
