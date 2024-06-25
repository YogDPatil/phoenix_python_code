import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_setup(request):
    supported_browser = ['chrome', 'firefox', 'safari', 'headlesschrome', 'headlessfirefox']
    base_url = 'http://phoenix.testautomationacademy.in'
    # os.environ.get("BROWSER", None) attempts to retrieve the value of the environment variable BROWSER.
    # 'os.environ' is a dictionary-like object in Python that contains all the environment variables.

    # export BROWSER=<browser_name> // set environment browser
    browser = os.environ.get("BROWSER", None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")
        # browser = 'chrome'

    browser = browser.lower()

    if browser not in supported_browser:
        raise Exception(f"Provided browser '{browser}' is not one of teh supported"
                        f"Supported are: {supported_browser}")
    if browser in ('chrome'):
        driver = webdriver.Chrome()
    elif browser in ('firefox'):
        driver = webdriver.Firefox()
    elif browser in ('safari'):
        driver = webdriver.Safari()
    elif browser in ('headlesschrome'):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_option)
    elif browser in ('headlessfirefox'):
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument('headless')
        driver = webdriver.Firefox(oprions=firefox_option)
    driver.get(base_url + "/sign-in")
    driver.maximize_window()
    # assign driver to class variable
    request.cls.driver = driver
    request.cls.base_url = base_url
    yield
    driver.quit()
