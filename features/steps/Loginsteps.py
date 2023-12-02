from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
import random
import string
# from numpy.distutils.command.config import config
# from pages.BasePage import BasePage
from Constants.TestConfig import TestData


@then(u'Verify update review button is displaying')
def verify_update_review_button(context):
    try:
        context.loginPage.verify_update_review_btn_on_dashboard_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify update review button is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify update review button is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify update review button is displaying"


@then(u'Verify that the email field is displaying a value')
def verify_login_button_is_working(context):
    try:
        context.loginPage.verify_field_have_value_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify that the email field is displaying a value"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify that the email field is displaying a value"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the email field is displaying a value"

@then(u'Login with valid email and password')
def verify_login_button_is_working(context):
    try:
        context.loginPage.enter_email_input_field_on_login_page(TestData.email)

        context.loginPage.enter_password_input_field_on_login_page(TestData.password)
        context.loginPage.click_login_button()
    except Exception as e:
        pass
        # attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Login with valid email"),
        #        attachment_type=AttachmentType.PNG)
        # context.driver.close()
        # assert False, e
    except:
        pass
        # attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Login with valid email"),
        #        attachment_type=AttachmentType.PNG)
        # context.driver.close()
        # assert False, "Test Failed on Login with valid email"

@then(u'Enter email in text field')
def verify_login_button_is_working(context):
    try:
        context.loginPage.enter_email_input_field_on_login_page(TestData.email)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on email in text field"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on email in text field"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on email in text field"

@then(u'Enter email "{value}" in text field')
def verify_enter_email_input_field_on_login_page(context, value):
    try:
        context.loginPage.enter_email_input_field_on_login_page(value)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Login with invalid email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Login with invalid email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Login with invalid email"

@then(u'Enter password "{value}" in password text field')
def verify_login_button_is_working(context, value):
    try:
        context.loginPage.enter_password_input_field_on_login_page(value)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Login with valid password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Login with valid password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Login with valid password"

@then(u'Verify that the password field is displaying a value')
def verify_login_button_is_working(context):
    try:
        context.loginPage.verify_field_have_value_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on VVerify that the password field is displaying a value"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify that the password field is displaying a value"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the password field is displaying a value"

@then(u'Verify that the password value "{value}" is unmaskable')
def verify_password_field_unmaskable_is_displayed(context, value):
    try:
        context.loginPage.verify_password_field_unmaskable_is_displayed(value)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify password field is unmaskable"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify password field is unmaskable"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify password field is unmaskable"

@then(u'click on password mask button')
def click_on_password_mask_button(context):
    try:
        context.loginPage.click_Password_mask_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on click on password mask button"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on click on password mask button"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on click on password mask button"

@then(u'Verify that the password field value "{value}" can be masked')
def verify_password_field_unmaskable_is_displayed(context, value):
    try:
        context.loginPage.verify_password_field_maskable_is_displayed(value)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify that the password field is maskable"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify that the password field is maskable"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the password field is maskable"

@then(u'click on remember me checkbox and verify remember me checkbox is checked')
def click_on_remember_me_checkbox_verify_remember_me_checkbox_is_checked(context):
    try:
        context.loginPage.click_on_remember_me_checkbox_verify_remember_me_checkbox_is_checked()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on click on remember me checkbox and verify remember me checkbox is checked"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on click on remember me checkbox and verify remember me checkbox is checked"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on click on remember me checkbox and verify remember me checkbox is checked"

@then(u'click on remember me checkbox and verify remember me checkbox is unchecked')
def click_on_remember_me_checkbox_verify_remember_me_checkbox_is_unchecked(context):
    try:
        context.loginPage.click_on_remember_me_checkbox_verify_remember_me_checkbox_is_unchecked()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on click on remember me checkbox and verify remember me uncheckbox is checked"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on click on remember me checkbox and verify remember me uncheckbox is checked"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on click on remember me checkbox and verify remember me uncheckbox is checked"

@then(u'click on forgot password button')
def click_on_forgot_password_button(context):
    try:
        context.loginPage.click_on_forgot_password_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on click on forgot password button"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on click on forgot password button"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on click on forgot password button"

@then(u'Verify that the forgot page is displayed')
def verify_forgot_Page_is_displayed(context):
    try:
        context.loginPage.verify_forgot_page_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify that the forgot page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on that the forgot page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the forgot page is displayed"

@then(u'click on create an account link')
def click_on_create_an_account_link(context):
    try:
        context.loginPage.click_on_create_an_account_link()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on create an account link"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on create an account link"),
                attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on create an account link"

@then(u'Verify that the create an account page is displayed')
def verify_Create_an_Account_Page_is_displayed(context):
    try:
        context.loginPage.verify_Create_an_Account_Page_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify that the create an account page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on that the create an account page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the create an account page is displayed"

@then(u'Verify that the home page is displayed')
def verify_Create_an_Account_Page_is_displayed(context):
    try:
        context.loginPage.verify_home_Page_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify that the home page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on that the home page is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify that the home page is displayed"

@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
