import pytest
import sys
import logging
from webdriver_helpers import *


class SeleniumPage:
	TIMEOUT = 10

	def __init__(self, driver:WebDriver, url):
		self.driver = driver
		self.wait = WebDriverWait(driver, self.TIMEOUT)
		self.setup_log()
		self.url = url

	def setup_log(self):
		logging.basicConfig()
		self.log = logging.getLogger(__class__.__name__)
		self.log.setLevel(logging.DEBUG)
		self.log.addHandler(logging.FileHandler("test.log"))
		# self.log.addHandler(logging.StreamHandler(sys.stdout))

	def open(self):
		self.driver.get(self.url)
		self.log.debug(f"opened page at {self.driver.current_url} with title: {self.driver.title}")

	def is_current_page(self):
		try:
			self.wait.until(expected.title_is(self.TITLE))
			return True
		except:
			self.log.debug(f"not on expected page {__class__.__name__}")
			return False

	def when_visible(self, locator):
		self.log.debug(f"wait until visible: {locator}")
		return self.wait.until(expected.visibility_of_element_located(locator))

	def when_clickable(self, locator):
		self.log.debug(f"wait until clickable: {locator}")
		return self.wait.until(expected.element_to_be_clickable(locator))

	def click(self, locator):
		self.when_clickable(locator).click()
