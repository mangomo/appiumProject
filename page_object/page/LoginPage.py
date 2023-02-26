from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.page.BasePage import BasePage


class LoginPage(BasePage):
    _close_locator = (AppiumBy.ID, "gt_one_login_nav_iv")
    _iv_action_back = (AppiumBy.ID, "iv_action_back")
    _phone_one_locator = (AppiumBy.ID, "gt_one_login_submit_tv")
    _switch_phone_locator = (AppiumBy.ID, "gt_one_login_switch_tv")
    _other_locator = (AppiumBy.ID, "tv_content")
    _register_phone_number = (AppiumBy.ID, "register_phone_number")
    _register_code_text = (AppiumBy.ID, "register_code_text")
    _register_code = (AppiumBy.ID, "register_code")
    _service_agreement = (AppiumBy.XPATH, "//*[@text='阅读并同意 服务协议、隐私政策']")
    _button_next = (AppiumBy.ID, "button_next")
    _login_without_password = (AppiumBy.ID, "login_without_password")
    _login_outside = (AppiumBy.ID, "login_outside")
    _weixin_login = (AppiumBy.ID, "weixin_login")
    _tencent_login = (AppiumBy.ID, "tencent_login")
    _sina_login = (AppiumBy.ID, "sina_login")
    _tv_mail_number = (AppiumBy.ID, "sina_login")
    _send_mail_code = (AppiumBy.ID, "send_mail_code")
    _tv_mail_login_code = (AppiumBy.ID, "tv_mail_login_code")
    _login_account = (AppiumBy.ID, "login_account")
    _login_password = (AppiumBy.ID, "login_password")
    _tv_forget_password = (AppiumBy.ID, "tv_forget_password")
    _error_msg = (AppiumBy.ID, "md_content")
    _md_buttonDefaultPositive = (AppiumBy.ID, "md_buttonDefaultPositive")
    _tv_agree = (AppiumBy.ID, "tv_agree")
    # 返回键二选一
    _back_btn = (
        AppiumBy.XPATH, "//*[contains(@resource-id,'gt_one_login_nav_iv') or contains(@resource-id,'iv_action_back')]")
    _guide_skip = (AppiumBy.ID, "new_user_guide_skip_tv")

    def loginByWX(self):
        return self

    def loginByTencent(self):
        return self

    def loginBySina(self):
        return self

    def loginByMail(self):
        return self

    def loginByAccount(self, account, password):
        self.find(self._switch_phone_locator).click()
        self.find(self._login_outside).click()
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        # 如果没有同意条款，则点击。同意则直接点button_next,此处checkbox中获取的get_attribute是string类型的
        # is_checked = self.find(self._service_agreement).get_attribute('checked')
        # if 'false' in is_checked:
        #     self.find(self._service_agreement).click()
        self.find(self._button_next).click()
        self.find(self._tv_agree).click()
        return self

    def loginSuccessByAccount(self, account, password):
        # 延时导入
        from page_object.page.MainPage import MainPage
        return MainPage()

    def loginByPhoneNumber(self, phone, code):
        return self

    def loginByOneKey(self):
        return self

    def service_agreement(self):
        return True

    def getErrorMsg(self):
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg

    def guideSkip(self):
        for i in range(1, 3):
            self.find(self._guide_skip).click()

    def back(self):
        # 显示等待：判断一个元素是否出现，等待2秒，找到后继续往下走。
        # WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(self._iv_action_back))
        self.find(self._back_btn).click()
        from page_object.page.WelcomePage import WelcomePage
        return WelcomePage()
