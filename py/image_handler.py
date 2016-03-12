from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def image_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/searchbyimage?&image_url=http://upload.wikimedia.org/wikipedia/commons/2/29/Voyager_spacecraft.jpg")
    guess = driver.find_element_by_class_name("_gUb").text
    driver.close()
    return guess
