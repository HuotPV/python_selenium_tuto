# The goal here is to do more advanced operation on the website (drag an drop, double click, and more ....)
# more info at https://selenium-python.readthedocs.io/api.html

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # this should enables us to "type" in our web page (in a search bar, a user email field ...)
import time
from selenium.webdriver.common.by import By ## Used in the "wait" try blocks
from selenium.webdriver.support.ui import WebDriverWait ## Used in the "wait" try blocks
from selenium.webdriver.support import expected_conditions as EC ## Used in the "wait" try blocks


PATH = '/home/pv/chromedriver'  # path to the webdriver
driver = webdriver.Chrome(PATH)  # call the webdriver defined in PATH

driver.get("http://orteil.dashnet.org/cookieclicker/")  # A new web page !!!

# it will be a way to perform a set of actions in one go ... 


try:
    langue = WebDriverWait(driver,5).until(                                        # wait a maximum of 5 s
        EC.presence_of_element_located((By.ID,'langSelect-FR'))  # for the text Beginner Python Tutorials to show up, and stores it in element
    )
finally:
    langue.click()   # then click the link

driver.implicitly_wait(8) # another way of waiting

cookie = driver.find_element_by_id('bigCookie')
cookies = driver.find_element_by_id('cookies')

items = [driver.find_elements_by_id('productPrice' + str(i) ) for i in range(1,-1,-1)]  # the upgrade have the id productPrice0, productPrice1, etc ... here we create a list of element starting from productPrice1 and going down...

actions = ActionChains(driver) #we create an ActionChains instance that will work on "driver"
actions.click(cookie)


for i in range(0,5000):
    actions.perform() # perform the action, that is, clicking the cookie.
    count = int(cookies.text.split(' ')[0])
    for item in items:
        value = int(item[0].text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item[0])
            upgrade_action.click()
            upgrade_action.perform()

time.sleep(5)
driver.quit()