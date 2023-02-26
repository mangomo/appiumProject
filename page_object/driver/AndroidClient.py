from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver: WebDriver

    @classmethod
    def installApp(cls) -> WebDriver:
        # 如果有必要，进行第一次安装
        caps = {}
        caps["appium:platformName"] = "Android"
        caps["appium:platformVersion"] = "11.0"
        caps["appium:deviceName"] = "mango"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["appium:autoGrantPermissions"] = True
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restartApp(cls) -> WebDriver:
        caps = {}
        caps["appium:platformName"] = "Android"
        caps["appium:platformVersion"] = "11.0"
        caps["appium:deviceName"] = "mango"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        # caps['appium:unicodeKeyboard'] = True
        # caps['appium:resetKeyboard'] = True
        # 为了更快的启动，并保留之前的数据
        caps["noReset"] = True
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
