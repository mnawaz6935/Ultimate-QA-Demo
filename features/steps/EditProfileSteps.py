import allure
from behave import *
from faker import Faker

@then("Click on the profile dropdown")
def step_impl(context):
    context.editMerchantPage.click_on_profile_dropdown()


@then("Click on My Account menu")
def step_impl(context):
    context.editMerchantPage.click_on_my_account_menu()


@then("Generate a random string")
def step_impl(context):
    context.random_string = f'{Faker().company()}'
    allure.attach(context.random_string, name='Random String', attachment_type=allure.attachment_type.TEXT)


@then("Generate a random professional title")
def step_impl(context):
    context.random_professional = f'{Faker().job()}'
    allure.attach(context.random_professional, name='Random Professional Title', attachment_type=allure.attachment_type.TEXT)

@then("Enter the '<RandomString>' in the company field")
def step_impl(context):
    context.editMerchantPage.enter_company_name(context.random_string)


@when("Click on the Save Changes button")
def step_impl(context):
    context.editMerchantPage.click_on_the_save_changes_button()


@then("Verify company field have same '<RandomString>' value")
def step_impl(context):
    context.editMerchantPage.verify_company_name_have_value(context.random_string)


@then("Enter the '<RandomString>' in the professional title field")
def step_impl(context):
    context.editMerchantPage.enter_professional_title(context.random_professional)


@then("Verify professional title field have same '<RandomString>' value")
def step_impl(context):
    context.editMerchantPage.verify_professioanl_title_have_value(context.random_professional)