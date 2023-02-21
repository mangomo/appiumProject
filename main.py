# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["appium:platformName"] = "Android"
caps["appium:platformVersion"] = "11.0"
caps["appium:deviceName"] = "mango"
caps["appium:appPackage"] = "com.xueqiu.android"
caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_agree")
el1.click()
driver.implicitly_wait(10)
el2 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/gt_one_login_check")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/gt_one_login_submit_layout")
el3.click()

driver.quit()