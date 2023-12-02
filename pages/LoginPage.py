import time
from Elements.LoginPageElements import LoginPageElements


class LoginPage(LoginPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        try:
            self.click_element(self.login_button)
        except:
            pass
        self.click_element(self.email_input_field_on_login_page)
        self.click_element(self.login_button)

    def enter_email_input_field_on_login_page(self, email):
        self.input_element(self.email_input_field_on_login_page, email)

    def enter_password_input_field_on_login_page(self, password):
        self.input_element(self.password_input_field_on_login_page, password)

    def verify_field_have_value_is_displayed(self):
        value = self.verify_field_have_value(self.email_input_field_on_login_page)
        if not value:
            assert False
        else:
            assert True

    def click_on_remember_me_checkbox(self):
        self.click_element(self.REMEMBER_ME_CHECKBOX)

    def click_on_remember_me_checkbox_verify_remember_me_checkbox_is_checked(self):
        get_value_before = self.is_element_selected(self.REMEMBER_ME_CHECKBOX)
        self.click_element(self.REMEMBER_ME_LINK)
        time.sleep(2)
        get_value_after = self.is_element_selected(self.REMEMBER_ME_CHECKBOX)
        if get_value_after != get_value_before:
            assert True
        else:
            assert False

    def click_on_remember_me_checkbox_verify_remember_me_checkbox_is_unchecked(self):
        self.click_element(self.REMEMBER_ME_LINK)
        time.sleep(2)
        get_value_before = self.is_element_selected(self.REMEMBER_ME_CHECKBOX)
        self.click_element(self.REMEMBER_ME_LINK)
        time.sleep(2)
        get_value_after = self.is_element_selected(self.REMEMBER_ME_CHECKBOX)
        if get_value_after != get_value_before:
            assert True
        else:
            assert False

    def click_on_forgot_password_button(self):
        self.click_element(self.FORGOT_LINK)

    def verify_forgot_page_is_displayed(self):
        value = self.verify_element_display(self.FORGOT_PAGE)
        if not value:
            assert False
        else:
            assert True

    def click_on_create_an_account_link(self):
        self.click_element(self.Create_an_Account)

    def verify_Create_an_Account_Page_is_displayed(self):
        value = self.verify_element_display(self.Create_an_Account_Page)
        if not value:
            assert False
        else:
            assert True

    def verify_home_Page_is_displayed(self):
        value = self.verify_element_display(self.home_Page)
        if not value:
            assert False
        else:
            assert True
