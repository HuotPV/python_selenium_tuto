from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit") # this refers to the HTML id of the GO button on python main page
                                  # here simply a tuple containing the method to search the go_button (By.ID) and the ID we should look for ("submit")

class SearchResultsPageLocators(object):
    pass
