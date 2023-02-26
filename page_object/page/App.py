from appium.webdriver.common.appiumby import AppiumBy

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage
from page_object.page.WelcomePage import WelcomePage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restartApp()
        return MainPage()

    @classmethod
    def start_WelcomePage(cls):
        cls.getClient().installApp()
        return WelcomePage()
