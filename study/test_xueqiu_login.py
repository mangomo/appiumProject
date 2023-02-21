# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import pytest
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# Xpath 尽量使用相对定位，可以后期维护。绝对定位后期不好维护测试用例
# 相对定位语法：//标签名[@属性名=属性值]
# 全局查找  //*[@text = "基金"]
# 全局搜索，多条件匹配 //*[@text = "基金" and @instance="4"]
# 根据父类id查找，查找父类id下的元素    //*[contains(@resource-id,"button_container")]//*[@text = "基金"]
# find_element_by_xpath("//input[@id='input']")


class TestXueqiuLogin(object):

    @classmethod
    def setup_class(cls):
        print("setup_class" + "----" + "被执行了")
        cls.init_appium()

    # @classmethod
    # def teardown_class(cls):
    #     print("teardown_class" + "----" + "被执行了")

    def setup_method(self):
        print("setup_method" + "----" + "被执行了")
        # 获取启动appium的driver实例，用于后续每个case的driver
        self.driver = self.restart_appium()

    # def teardown_method(self):
    #     print("teardown_method" + "----" + "被执行了")
    #     # 不加也行，如果不quit，启动appium会自动quit之前的session
    #     self.driver.quit()

    @classmethod
    def init_appium(cls) -> WebDriver:
        # 如果有必要，进行第一次安装
        caps = {}
        caps["appium:platformName"] = "Android"
        caps["appium:platformVersion"] = "11.0"
        caps["appium:deviceName"] = "mango"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["appium:autoGrantPermissions"] = True

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {}
        caps["appium:platformName"] = "Android"
        caps["appium:platformVersion"] = "11.0"
        caps["appium:deviceName"] = "mango"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        # 为了更快的启动，并保留之前的数据
        caps["noReset"] = True
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    def test_login(self):
        el1 = self.driver.find_element(by=AppiumBy.ID, value="tv_agree")
        el1.click()
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element(by=AppiumBy.ID, value="gt_one_login_check")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="gt_one_login_submit_layout")
        el3.click()

    def test_swipe(self):
        # 原始的滑动方法
        for i in range(5):
            self.driver.swipe(900, 900, 100, 100)
            time.sleep(2)

    # def test_touchction(self):
    #     action = TouchAction(self.driver)
    #     for i in range(3):
    #         action.press(x=800, y=800).move_to(x=100, y=100).wait(1000).release().perform()

    def test_touchaction_p(self):
        rect = self.driver.get_window_rect()
        action = TouchAction(self.driver)
        for i in range(5):
            # action.press滑动没有效果，要用action.long_press才有滑动效果
            action.long_press(x=rect['width'] * 0.8, y=rect['height'] * 0.8).move_to(x=0, y=0).release()
            action.perform()
            time.sleep(2)

    def test_inputtext(self):
        el1 = self.driver.find_element(by=AppiumBy.ID, value="action_message")
        el1.click()
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element(by=AppiumBy.ID, value="rl_list_item_container")
        el2.click()
        # 截图
        self.driver.get_screenshot_as_file("screenshot" + ".png")
        self.driver.back()  # 手机的物理键后退
