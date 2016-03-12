from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

def image_crop():
    main = Image.open("main.jpg")
    size = main.size()
    main.crop(0, 0, size[0], 3 * size[1] / 4).save("crop1.jpg")
    main.crop(0, size[1] / 4, size[0], size[1]).save("crop2.jpg")
    main.crop(size[0] / 4, 0, size[0], size[1]).save("crop1.jpg")
    main.crop(0, 0, 3 * size[0] / 4, size[1]).save("crop1.jpg")

def image_search(image_url):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/searchbyimage?&image_url=" + image_url)
    guess = driver.find_element_by_class_name("_gUb").text
    driver.close()
    return guess

def get_guess():
    image_crop()
    guesses = [image_search("main.jpg"),
               image_search("crop1.jpg"),
               image_search("crop2.jpg"),
               image_search("crop3.jpg"),
               image_search("crop4.jpg")
               ]
    counts = [guesses.count(guess) for guess in guesses]
    return guesses[count.index(max(count))]
