# The goal here is to navigate the website, clikc link and buttons, and return to the main page ..

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # this should enables us to "type" in our web page (in a search bar, a user email field ...)
import time
from selenium.webdriver.common.by import By ## Used in the "wait" try blocks
from selenium.webdriver.support.ui import WebDriverWait ## Used in the "wait" try blocks
from selenium.webdriver.support import expected_conditions as EC ## Used in the "wait" try blocks



PATH = '/home/pv/chromedriver'  # path to the webdriver
driver = webdriver.Chrome(PATH)  # call the webdriver defined in PATH

driver.get("https://techwithtim.net")  # open a web page and go to the specified link

link = driver.find_element_by_link_text("Python Programming") # allows to find a link by the text showed up for this link ...
link.click() # click the link

try:
    element = WebDriverWait(driver,5).until(                                        # wait a maximum of 5 s
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))  # for the text Beginner Python Tutorials to show up, and stores it in element
    )
finally:
    element.click()   # then click the link

try:
    element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))    # we found the id of the button we want to click by inspecting the HTML page, we wait for it to load, we store it in element ...
    )
finally:
    element.click()  # ... and we click the button

driver.back() # go back one page (we are in Beginner Python Tutorials now)
time.sleep(2)
driver.back() # go back one more page (we are in Python Programming now)
time.sleep(2)
driver.back() # go back one final page, we should be on the main page now !
time.sleep(2)
driver.forward() # go forward again (in Python Programming again)
time.sleep(2)
driver.forward() # one more forward (in Beginner Python Tutorials now)
 
time.sleep(5)
driver.quit()