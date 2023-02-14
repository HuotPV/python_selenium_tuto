from locator import *
from element import BasePageElement

class GoButtonElement(BasePageElement):
    locator="go"

class SearchTextElement(BasePageElement):
    locator="q"   # "q" is the name of the search bar on the python webpage HTML code

class BasePage(object):
    # a class instance will be made for each page
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)  # we use the general method find_element here. 
                                                                         # The way to find the element is actually located in the MainPageLocators.GO_BUTTON tuple. 
                                                                         # The "*" is used to unpack the tuple and to split it into two arguments.
        element.click()

class SearchResultPage(BasePage):

    def is_result_found(self):
        return "No results found." not in self.driver.page_source # check if the search actually works