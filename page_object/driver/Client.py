import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Client(object):
    driver: WebDriver
    platform = "android"

    @classmethod
    def installApp(cls) -> WebDriver:
        '''
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
        '''
        cls.initDriver("installApp")

    @classmethod
    def restartApp(cls) -> WebDriver:
        '''
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
        '''
        cls.initDriver("restartApp")

    @classmethod
    def initDriver(cls, key):
        driver_data = yaml.load(open("../data/Driver.yaml", "r", encoding="utf-8"), Loader=yaml.FullLoader)
        platform = str(driver_data['platform'])
        cls.platform = platform
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        caps = driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver
