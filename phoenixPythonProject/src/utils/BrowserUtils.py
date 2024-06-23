from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 30)
        self.default_timeout = 10

    def enterText(self, locator, text, timeout=None):

        # TYPE 1 webdriver wait use
        # self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

        # TYPE 2 webdriver wait use
        # set timeout as default if timeout is not mention in method argument
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator)).send_keys(
            text)

    def clickOn(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()
