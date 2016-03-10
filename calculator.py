#You can use Unit Test or Nose. I'm using Nose
#import the things we need
import nose
#import unittest
from selenium import webdriver
import contextlib
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()

#Just validating the webdriver can successfully use the site
#All test names must start with "test"
def test_keys():
    #Ultimately something like this would actually live in a source url file that way we don't have it for every test in every file.
    driver.get("http://pocket-calculator.herokuapp.com/")
    driver.set_page_load_timeout(120)
    time.sleep(2.0)
    #Find the image contained in the div next to the requirement status, make sure it's a check mark
    #xpath is the most reliable way to find this because it stays the most constant
    element = driver.find_element_by_xpath("//*[contains(@class, 'calculator-display')]")
    #Does the image I'm looking out contain what I'm expecting in its source?
    result = element.text
    print result
    
if __name__ == "__main__":
    #unittest.main()
    nose.main()