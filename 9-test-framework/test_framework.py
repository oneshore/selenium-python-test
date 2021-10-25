import pytest
from base_framework import BaseFramework

class TestFramework(BaseFramework):

	@pytest.fixture
	def get_browser(self, driver):
		self.driver = driver
		self.setup()

	def test_launch_browser(self):
		self.driver.get("https://shop.one-shore.com")
		self.log.info(self.driver.title)
