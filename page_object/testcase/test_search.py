import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mianPage = App.main()

    def setup_method(self):
        self.mianPage: MainPage = TestSelected.mianPage
        self.searchPage = self.mianPage.gotoSearch()


    def test_is_selected_stock(self):
        self.searchPage.search("alibaba")
        assert self.searchPage.isInSelected("BABA") == True
        assert self.searchPage.isInSelected("88") == False

    @pytest.mark.parametrize("key,code", [
        ("万达电影", "SZ002739"),
        ("宁德时代", "SZ300750"),
        ("得润电子", "SZ002055")
    ])
    def test_is_selected_stock_hs(self, key, code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code) == True

    def teardown_method(self):
        self.searchPage.cancel()

    def test_add_selected_stock_hs(self):
        key = "万达电影"
        stock_code = "SZ002739"
        searchPage = self.searchPage.search(key)
        if searchPage.isInSelected(stock_code):
            searchPage.removeFromSelected(stock_code)
        searchPage.addToSelected(stock_code)
        assert searchPage.isInSelected(stock_code) == True
