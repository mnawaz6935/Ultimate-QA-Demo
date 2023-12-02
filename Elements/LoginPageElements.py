from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPageElements(BasePage):
    login_button = (By.XPATH, "//button[contains(text(),'Sign in')]")
    email_input_field_on_login_page = (By.XPATH, "//input[@id='user[email]']")
    password_input_field_on_login_page = (By.XPATH, "//input[@id='user[password]']")
    REMEMBER_ME_LINK = (By.XPATH, '//label[@for="user[remember_me]"]')
    REMEMBER_ME_CHECKBOX = (By.XPATH, '//input[@id="user[remember_me]"]')
    FORGOT_LINK = (By.XPATH, '//a[@href="/users/password/new"]')
    FORGOT_PAGE = (By.XPATH, "//h2[contains(text(),'Forgot your Password?')]")
    Create_an_Account = (By.XPATH, '//a[@href="/users/sign_up"]')
    Create_an_Account_Page = (By.XPATH, '//h2[contains(text(),"Create a new account")]')
    home_Page = (By.XPATH, '(//*[contains(text(),"My Dashboard")])[1]')
