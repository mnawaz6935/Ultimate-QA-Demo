import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from Constants.TestConfig import TestData
from Constants.TestConfig import userdata
from pages.LoginPage import LoginPage
from pages.BasePage import BasePage
from pages.EditProfilePage import EditMerchantPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path

home_directory = Path(__file__).resolve().parent.parent.parent


@given(u'Launch the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": f"{home_directory}\TestData",
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("prefs", prefs)
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        if TestData.PLATFORM == 'Browser Stack':
            desired_cap = {
                'os_version': '10',
                'resolution': '1920x1080',
                'browser': 'Firefox',
                'browser_version': '90.0',
                'os': 'Windows',
                'name': 'BStack-[Python] Sample Test',  # test name
                'build': 'BStack Build Number 1'  # CI/CD job or build name
            }
            context.driver = webdriver.Remote(
                command_executor='https://{User_name}:{Key}@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=desired_cap)
        elif TestData.PLATFORM == 'local':
            service = Service(executable_path=ChromeDriverManager().install())
            context.driver = webdriver.Chrome(service=service, options=options)
        elif TestData.PLATFORM == 'Docker':
            remote_url = os.getenv('SELENIUM_GRID_URL')
            time.sleep(5)
            context.driver = webdriver.Remote(command_executor=f'http://{remote_url}/wd/hub',
                                              desired_capabilities=DesiredCapabilities.CHROME, options=options)
        context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


@when(u'Open the https://courses.ultimateqa.com/users/sign_in')
def open_login_page(context):
    try:
        context.driver.get(userdata.url)
        context.loginPage = LoginPage(context.driver)
        context.BasePage = BasePage(context.driver)
        context.editMerchantPage = EditMerchantPage(context.driver)
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test is failed in open section"
