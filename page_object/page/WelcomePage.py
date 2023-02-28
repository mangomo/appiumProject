import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class WelcomePage(BasePage):
    _tv_agree = (AppiumBy.ID, "tv_agree")

    def gotoProfile(self):

        pass

    def gotoLogin(self):
        try:
            element = self.find(self._tv_agree)
        except NoSuchElementException as e:
            print(e)
            self.loadSteps('/data/WelcomePage.yaml', 'gotoLogin')
            time.sleep(1)
        else:
            element.click()
            time.sleep(1)
        return LoginPage()
