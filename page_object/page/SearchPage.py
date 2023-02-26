from appium.webdriver.common.appiumby import AppiumBy

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    # 页面全局只有一个EditText，所以这里可以用CLASS_NAME来查找元素
    _edit_locator = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def search(self, key):
        self.find(self._edit_locator).send_keys(key)
        search_button = "搜索"
        self.findByText(search_button).click()
        # 返回self为了以后链式调用
        return self

    def addToSelected(self, key):
        follow_button = (AppiumBy.XPATH,
                         "//*[contains(@resource-id,'stock_code_tv') and contains(@text ,'%s')]/../..//*[contains(@resource-id,'follow_btn')]" % key)
        self.find(follow_button).click()
        return self

    def removeFromSelected(self, key):
        follow_button = (AppiumBy.XPATH,
                         "//*[contains(@resource-id,'stock_code_tv') and contains(@text ,'%s')]/../..//*[contains(@resource-id,'followed_btn')]" % key)
        self.find(follow_button).click()
        return self

    def isInSelected(self, key):
        # 根据stock_code，找到关注button的状态
        follow_button = (AppiumBy.XPATH,
                         "//*[contains(@resource-id,'stock_code_tv') and contains(@text ,'%s')]/../..//*[contains(@resource-id,'follow')]" % key)
        # 获取follow-button的resourceId值
        id = self.find(follow_button).get_attribute('resourceId')
        print(id)
        # 返回是否followed
        return "followed_btn" in id

    def cancel(self):
        # candel_button = (AppiumBy.ID, "com.xueqiu.android:id/action_delete_text")
        # self.find(candel_button).click()
        self.driver.back()
