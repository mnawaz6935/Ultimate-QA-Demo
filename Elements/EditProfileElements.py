from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class EditMerchantPageElements(BasePage):
    profile_dropdown = (By.XPATH, '(//*[@aria-controls="header-dropdown-menu"])[last()]')
    MY_ACCOUNT_MENU = (By.XPATH, '//a[@href="/account"]')
    COMPANY_NAME = (By.XPATH, '//input[@id="user[profile_attributes][company]"]')
    PROFESSIONAL_TITLE = (By.XPATH, '//input[@id="user[profile_attributes][headline]"]')
    SAVE_CHANGES_BUTTON = (By.XPATH, '//input[@value="Save Changes"]')
