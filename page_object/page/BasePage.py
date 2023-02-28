import os

import yaml
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import Client


class BasePage(object):
    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = Client.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return Client

    def find(self, kv) -> WebElement:
        # todo: 处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((AppiumBy.XPATH, "//*[@text='%s']" % text))

    def loadSteps(self, po_path, key, **kwargs):
        base_path = os.path.dirname(os.path.abspath('.'))
        file = open(base_path + po_path, "r", encoding="utf-8")
        po_data = yaml.load(file, Loader=yaml.FullLoader)
        po_method = po_data[key]
        # po_elements=yaml.load(open('xxx.yaml'))['elements']
        if po_data.keys().__contains__("elements"):
            po_elements = po_data['elements']
        for step in po_method:
            step: dict
            element_platform = dict()
            if step.keys().__contains__('element'):
                element_platform = po_elements[step['element']][Client.platform]
            else:
                element_platform = {"by": step['by'], "locator": step['locator']}
            element: WebElement = self.driver.find_element(by=element_platform['by'], value=element_platform['locator'])
            action = str(step['action']).lower()
            # todo:弹框处理，元素智能等待
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                    print("update text:  new:%s " % text)
                element.send_keys(text)
            else:
                print("UNKNOWN COMMAND %s" % step)
