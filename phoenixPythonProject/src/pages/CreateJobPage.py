from phoenixPythonProject.src.utils.BrowserUtils import BrowserUtils


class CreateJobPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getCreateJobPageUrl(self,page_name):
        return self.getCurrentPageUrl(page_name)


