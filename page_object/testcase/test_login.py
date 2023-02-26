import time

import pytest

from page_object.page.App import App


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.WelcomePage = App.start_WelcomePage()

    def setup_method(self):
        self.loginPage = self.WelcomePage.gotoLogin()

    @pytest.mark.parametrize("account,password,msg", [
        ("176111122220", "123456", "手机号码填写错误"),
        ("17611008070", "123456", "用户名或密码错误")
    ])
    def test_login_account(self, account, password, msg):
        self.loginPage.loginByAccount(account, password)
        assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.loginPage.back()
        self.loginPage.guideSkip()