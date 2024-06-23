import pytest
from phoenixPythonProject.src.pages.SigninPage import SignInPage



@pytest.mark.usefixtures("driver_setup")
class TestLoginPage():

    def test_validateLoginByUi(self):
        signinPage=SignInPage(self.driver)
        signinPage.doLogin('iamfd', 'password')

