import selenium
from selenium import webdriver

PATH = '/home/pv/chromedriver'  # path to the webdriver
driver = webdriver.Chrome(PATH)  # call the webdriver defined in PATH

driver.get("https://techwithtim.net")  # open a web page and go to the specified link

print(driver.title) # get page title

driver.close() # close browser's current tab
driver.quit() # close browser