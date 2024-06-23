import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_setup(request):
    supported_browser = ['chrome', 'firefox', 'safari']
    # os.environ.get("BROWSER", None) attempts to retrieve the value of the environment variable BROWSER.
    # 'os.environ' is a dictionary-like object in Python that contains all the environment variables.
    browser = os.environ.get("BROWSER", None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

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
    driver.get("http://phoenix.testautomationacademy.in/sign-in")
    driver.maximize_window()
    # assign driver to class variable
    request.cls.driver = driver
    yield
    driver.quit()
