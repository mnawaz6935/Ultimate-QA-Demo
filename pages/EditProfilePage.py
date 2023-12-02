from selenium.webdriver.common.by import By
from Elements.EditProfileElements import EditMerchantPageElements
from datetime import datetime
import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.TestConfig import TestData


class EditMerchantPage(EditMerchantPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_profile_dropdown(self):
        self.click_element(self.profile_dropdown)

    def click_on_my_account_menu(self):
        self.click_element(self.MY_ACCOUNT_MENU)

    def enter_company_name(self, name):
        self.input_element(self.COMPANY_NAME, name)

    def enter_professional_title(self, name):
        self.input_element(self.PROFESSIONAL_TITLE, name)
    def click_on_the_save_changes_button(self):
        self.click_element(self.SAVE_CHANGES_BUTTON)

    def verify_company_name_have_value(self, name):
        c_value = self.get_attribute_of_a_element(self.COMPANY_NAME, 'value')
        if name.lower() == c_value.lower():
            assert True
        else:
            assert False

    def verify_professioanl_title_have_value(self, name):
        c_value = self.get_attribute_of_a_element(self.PROFESSIONAL_TITLE, 'value')
        if name.lower() == c_value.lower():
            assert True
        else:
            assert False

