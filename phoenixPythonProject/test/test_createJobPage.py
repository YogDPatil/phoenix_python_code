import pytest

from phoenixPythonProject.src.pages.SigninPage import SignInPage

@pytest.mark.usefixtures("driver_setup")
class TestCreateJobPage:

    @pytest.mark.createJobPage
    def test_userRedirectsToCreateJobPage(self):
        signinPage = SignInPage(self.driver)
        assert signinPage.doLogin("iamfd", "password").clickOnCreateJobLink().getCreateJobPageUrl("create-job")
