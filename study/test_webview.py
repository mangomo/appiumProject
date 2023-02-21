# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Xpath 尽量使用相对定位，可以后期维护。绝对定位后期不好维护测试用例
# 相对定位语法：//标签名[@属性名=属性值]
# 全局查找  //*[@text = "基金"]
# 全局搜索，多条件匹配 //*[@text = "基金" and @instance="4"]
# 根据父类id查找，查找父类id下的元素    //*[contains(@resource-id,"button_container")]//*[@text = "基金"]
# find_element_by_xpath("//input[@id='input']")


class TestWebview(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print("setup_class" + "----" + "被执行了")
        cls.driver = cls.restart_appium()

    def setup_method(self):
        print("setup_method" + "----" + "被执行了")
        self.driver = TestWebview.driver
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='我的']").click()

    def teardown_method(self):
        print("teardown_method" + "----" + "被执行了")
        # 不加也行，如果不quit，启动appium会自动quit之前的session
        # self.driver.back()

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

    def test_webview(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='股票']").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='更多券商开户']").click()
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(MobileBy.ID, "更多券商开户"))
