from time import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')

driver.get("https://google.com")


search_text_box = driver.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("highest mountain in the world")
# "python selenium integration"
search_text_box.send_keys(Keys.RETURN)

sleep(5) # this is so we can see the results before we close
# Closes the current window
driver.close()
# All windows related to driver instance will quit
#driver.quit()
# when update chrome 3.9 --> put new 3.9 driver into python folder

