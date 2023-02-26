from appium.webdriver.common.appiumby import AppiumBy

from page_object.page.BasePage import BasePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    _search_botton = (AppiumBy.ID, "home_search")

    def gotoSelected(self) -> SelectedPage:
        zixuan = "自选"
        self.findByText(zixuan)
        self.findByText(zixuan).click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        self.find(self._search_botton).click()
        return SearchPage()
