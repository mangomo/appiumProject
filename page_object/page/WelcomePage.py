from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class WelcomePage(BasePage):
    _loginButton = (AppiumBy.ID, "tv_login")
    _tv_agree = (AppiumBy.ID, "tv_agree")

    def gotoProfile(self):
        pass

    def gotoLogin(self):
        try:
            element = self.find(self._tv_agree)
        except NoSuchElementException as e:
            print(e)
            self.find(self._loginButton).click()
        else:
            element.click()
        return LoginPage()
