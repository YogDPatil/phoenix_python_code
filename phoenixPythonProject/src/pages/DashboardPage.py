import time

from selenium.webdriver.common.by import By

from phoenixPythonProject.src.pages.CreateJobPage import CreateJobPage
from phoenixPythonProject.src.utils.BrowserUtils import BrowserUtils


class DashboardPage(BrowserUtils):
    user_icon_locator = (By.XPATH, "//mat-icon[@data-mat-icon-name='user-circle']/../../..")
    signin_username_locator = (By.XPATH, "//span[contains(text(),'Signed in')]/following-sibling::span")
    createjob_page_link_locator = (By.XPATH, "//span[contains(text(),'Create Job')]/../../..")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getDashboardPageUrl(self, text):
        return self.getCurrentPageUrl(text)

    def getSiginUsername(self):
        self.clickOn(self.user_icon_locator)
        return self.getElementText(self.signin_username_locator)

    def clickOnCreateJobLink(self):
        self.clickOn(self.createjob_page_link_locator)
        return CreateJobPage(self.driver)