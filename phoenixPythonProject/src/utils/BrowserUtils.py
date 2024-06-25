import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.default_timeout = 10

    def enterText(self, locator, text):
        timeout = None
        # TYPE 1 webdriver wait use
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).clear()
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)
        if timeout is not None:
            timeout = self.default_timeout
        print(timeout)
    def clickOn(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located((locator))).click()

    def getCurrentPageUrl(self, text):
        # time.sleep(1)
        return self.wait.until(expected_conditions.url_contains(text))

    def getElementText(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text
