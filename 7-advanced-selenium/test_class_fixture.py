import pytest
from time import sleep
from socket import gethostname
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select

def running_on_python_anywhere():
	if "console" in gethostname():
		return True
	return False

@pytest.fixture()
def headless():
	if running_on_python_anywhere():
		return True
	return False

# fixtures can request other fixtures
@pytest.fixture()
def options(headless):
	options:ChromeOptions = ChromeOptions()
	if headless:
		options.add_argument("--headless")
		options.add_argument("--disable-gpu")
	return options


# fixtures can be automatically applied to tests
@pytest.fixture()
def browser(options):
	browser = webdriver.Chrome(chrome_options=options)
	browser.implicitly_wait=10
	browser.maximize_window()
	yield browser
	sleep(2)
	# if error:
	# 	browser.save_screenshot()
	browser.quit()

def test_function(browser):
	browser.get("https://one-shore.com")
	print(browser.title)

class TestClass:

	def test_google(self, browser):
		browser.get("https://google.com")
		print(browser.title)

	def test_pythonanywhere(self, browser):
		browser.get("https://pythonanywhere.com")
		print(browser.title)


class TestClassFixture:

	@pytest.fixture(autouse=True)
	def setup(self, browser):
		self.browser = browser

	def test_shop(self):
		self.browser.get("https://shop.one-shore.com")
		print(self.browser.title)


