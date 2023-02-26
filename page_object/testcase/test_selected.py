from page_object.page.App import App


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mianPage = App.main()

    def test_price(self):
        assert self.mianPage.gotoSelected().gotoHS().getPriceByName("格力电器") == 36.56