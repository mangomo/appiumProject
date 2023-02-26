from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):

    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        # todo: 处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((AppiumBy.XPATH, "//*[@text='%s']" % text))
