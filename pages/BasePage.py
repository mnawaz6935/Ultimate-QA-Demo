import logging
import time
from logging import Logger

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from datetime import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        self.wait(1)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator))
        self.wait(2)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'})", element)
        self.wait(2)
        element.click()

    def click_using_js(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'})", element)
        self.driver.execute_script("arguments[0].click();", element)

    def input_element(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        self.wait(2)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'})", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL, '\A',
                                                                                                     '\b')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def is_element_selected(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        is_selected = self.driver.execute_script("return arguments[0].checked;",element)
        logging.info(f'Checkbox checked : {is_selected}')
        return is_selected

    def verify_element_display(self, by_locator):
        self.wait(2)
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).is_displayed()
            return True
        except:
            return False

    def verify_element_not_display(self, by_locator):
        self.wait(2)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).is_displayed()
            if not element:
                return True
        except:
            return False

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return element.is_enabled()

    def get_web_element(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_web_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def wait(self, seconds=3):
        time.sleep(seconds)

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def assert_equal(self, actual_value, expected_value, Message):
        assert actual_value == expected_value, Message

    def verify_element_disabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return not (element.is_enabled())

    def generate_random_email(self, value):
        digits = random.randint(1000, 9999)
        return str(value) + str(digits) + '@getnada.com'

    def generate_random_password(self, value):
        digits = random.randint(1000, 9999)
        return str(value) + str(digits)

    def generate_random_data_against_a_keyword(self, value):
        digits = random.randint(1000, 9999)
        return str(value) + str(digits)

    def get_attribute_of_a_element(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def generate_random_phone_number(self):
        digits = random.randint(1000000, 9999999)
        return '1613' + str(digits)

    def verify_field_have_value(self, by_locator):
        self.wait(2)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)).click()
        except:
            print('Unable to click')
            # self.driver.find_elements(By.XPATH, locator[1])[-1].click()

    def get_attribute_value(self, locator, attribute):
        if not isinstance(attribute, str):
            attribute = str(attribute)
        return self.driver.find_element(By.XPATH, locator).get_attribute(attribute)

    def select_by_text(self, by_locator, text):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_by_index(self, by_locator, index):
        # Wait for the element to be clickable
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        # Create a Select object to interact with the dropdown
        select = Select(select_element)
        time.sleep(5)
        # Select the option by index
        select.select_by_index(index)

    def get_selected_option_text(self, by_locator):
        # Wait for the element to be present and visible
        select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        # Create a Select object to interact with the dropdown
        select = Select(select_element)
        # Get the selected option's text
        selected_option = select.first_selected_option
        val = selected_option.text
        return val

    def is_date_between(self,start_date_str, end_date_str, target_date_str):
        # Parse the date strings into datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d')
        # Check if the target date is within the range
        return start_date <= target_date <= end_date

    def is_date_before(self,target_date_str, end_date_str):
        try:
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            return target_date <= end_date
        except ValueError:
            return False

    def convert_date_format(self,original_date_str):
        # Parse the original date string into a datetime object
        date_format = "%b %dth, %Y"
        original_date = datetime.strptime(original_date_str, date_format)

        # Convert the datetime object back to the desired format
        converted_date_str = original_date.strftime('%Y-%m-%d')

        return converted_date_str

    def convert_date_format_In_y_m_d(self,original_date):
        try:
            # Convert the input date to a datetime object using strptime
            date_format = "%m-%d-%y"
            date_object = datetime.strptime(original_date, date_format)

            # Convert the datetime object back to the desired format
            converted_date = date_object.strftime('%Y-%m-%d')

            return converted_date
        except ValueError:
            return "Invalid date format. Please provide a date in the format 'MM-DD-YYYY'."

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def click_with_action_chains(self, locator):
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click(element).perform()