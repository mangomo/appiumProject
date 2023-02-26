from appium.webdriver.common.appiumby import AppiumBy

from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self

    def getPriceByName(self, name) -> float:
        # todo:从页面中找到元素,根据name找到price
        '''

        :param name: self.driver.find_element(AppiumBy.XPATH,value="//*[contains(@resource-id,'portfolio_stockName') and @text = '" + name + "']/../../../..//*[contains(@resource-id,'item_layout')]").text
        :return: price
        '''
        name = (AppiumBy.XPATH,
                "//*[contains(@resource-id,'portfolio_stockName') and @text = '%s']/../../../..//*[contains(@resource-id,'item_layout')]" % name)
        price = self.find(name).text
        return float(price)
