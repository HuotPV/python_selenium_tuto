import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase): # create a class that inherit from unittest.TestCase class

    def setUp(self): # run before each test
        self.driver = webdriver.Chrome('/home/pv/chromedriver') 
        self.driver.get("http://www.python.org")

    def tearDown(self): # run after each test
        self.driver.close()

    def test_example(self): # tests methods have to start with "test_"
        print('this will print')
        assert True

    def test_search(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

if __name__ == "__main__":
    unittest.main()
