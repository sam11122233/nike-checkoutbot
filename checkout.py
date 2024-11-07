from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

PATH = './chromedriver'

driver = webdriver.Chrome (PATH)

print ('opening webpage ... ')

driver.get ('https://www.nike.com/launch/t/dunk-high-wu-tang-clan')

# wait 7 seconds for page to load
time.sleep (10)

print ("Searching for Size selector ... ")
shoeSize = driver.find_elements_by_class_name ("css-xf3ahq")
print ("Number of elements found:", len (shoeSize))
shoeSize[4].click ()

addToBag = driver.find_element_by_class_name ("add-to-cart-btn")
addToBag.click ()

# wait 3 seconds after clicking the button
time.sleep (5)

driver.get ('https://www.nike.com/cart')


time.sleep (5)
