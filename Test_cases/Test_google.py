import pytest
from selenium import webdriver

@pytest.mark.regression
def test_google(setup):
    #self.logger.info("**************** Title verification Page***************")
    driver = setup

    driver.get("http://www.google.com")
    gtitle=driver.title
    print(gtitle)