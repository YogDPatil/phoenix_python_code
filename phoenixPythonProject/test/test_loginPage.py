import pytest
from phoenixPythonProject.src.pages.SigninPage import SignInPage
# from phoenixPythonProject.src.helpers.PageObjects import ObjectClass


@pytest.mark.usefixtures("driver_setup")
class TestLoginPage():

    @pytest.mark.loginpage
    def test_validateLoginByUi(self):
        signinPage = SignInPage(self.driver)
        # dasboardPageUrl = signinPage.doLogin('iamfd', 'password').getDashboardPageUrl('dashboard')
        # assert dasboardPageUrl == self.base_url + "/frontdesk/dashboard"
        assert signinPage.doLogin('iamfd', 'password').getSiginUsername() == 'iamfd'
