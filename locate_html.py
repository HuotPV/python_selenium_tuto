# the goal here is to be able to find/locate/get elements of the webpage (button, search bars, etc ...)

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

# to locate an element, we would need its id, name, or class (a unique reference to the object, or if it does not exist, the best thing we can find ...)
# for this we need to know what is done in the page HTML code ...
# it can be done by right clicking elements on the page and click "inspect"
# Say we have a search bar whose name is "s", what we can try to do is:

search = driver.find_element_by_name("s")  # try to find the element whose name is "s" (on techwithtim's website, on 14/02/2023, it refers to a searchbar)
search.clear() # a usefull method that clear the field to be sure that there will only be what we want in the search bar
search.send_keys("test")  # type the string "test" in the searchbar
search.send_keys(Keys.RETURN) # press enter to execute the search

# search = driver.find_element_by_name("scrapbooking") # If no object match the selected search, we have an error.


# What we will try to do now is to get a specific element of the page obtained after typing "test" in the search bar.
# This is done in the "finally" block of the following "try" block.
# A potential issue we might have is that python will try to get the element we want before the page had time to load, resulting in a crash.
# To avoid this issue, we can use the selenium "waits" to wait for the page to load our element before attempting to accessing it.
# This is what the try block below is for. Note that it requires additional "imports".
# see this page for more details: https://selenium-python.readthedocs.io/waits.html
try:
    main = WebDriverWait(driver,10).until(                   # wait a maximum of 10 s
        EC.presence_of_element_located((By.ID,"main"))   
    )
finally:
    # typing "test" in the search bar sends us to a page with a list of blog post. The element holding all the blog post has an id equals to "main".
    # we can thus use this id to find this specific element:
    main = driver.find_element_by_id("main") # find the element with id main on the page showing up after searching "test"
    print(main.text) # print all the text of main.  

    print('----------------------------------------------------')

    # Now we will try to print the summary of the articles obtained with the search for "test"
    articles = main.find_elements_by_tag_name("article")  # we look for elements with tag_name "article" ... NOTE the use of elementS instead of element here.

    for article in articles:
        header = article.find_element_by_class_name("entry-summary") # get the entry-title class within each article
        print(header.text) # print the text ...


time.sleep(5) # wait 5 s so we can see what happens in the browser ...

# print(driver.page_source) # print the whole page HTML source code ... one other way to find elements !


driver.quit() # close browser