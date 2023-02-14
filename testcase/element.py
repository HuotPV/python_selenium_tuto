from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    def __set__(self,obj,value):    ## here we have redefined the __set__ method for the BasePageElement.
                                    ## that is, if we have an instance of BasePageElement named for example myElement
                                    ## we can do myElement = "toto"  and this will set the value of myElement to toto ...
                                    ## for instance, if myElement is a SearchTextElement (a search bar), doing myElement = "toto" will type "toto" into the search bar
                                    ## it works a bit like the overloading of operators in c++
        driver = obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):  ## same as above, the "__" "__" modify the get method, so that    a = myElement will get the value of the element and assign it to "a"
        driver = obj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribut("value")