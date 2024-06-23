from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from phoenixPythonProject.src.utils.BrowserUtils import BrowserUtils


class SignInPage(BrowserUtils):
    username_textbox_locator = (By.ID, "username")
    password_textbox_locator = (By.ID, "password")
    signin_button_locator = (By.XPATH, "//span[contains(text(),'Sign in')]/../.. ")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def doLogin(self, username, password):
        self.enterText(self.username_textbox_locator, username)
        self.enterText(self.password_textbox_locator, password)
        self.clickOn(self.signin_button_locator)