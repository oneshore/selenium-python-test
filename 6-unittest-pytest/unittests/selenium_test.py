import unittest
from selenium import webdriver

class SeleniumTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_open_demo_shop(self):
		self.driver.get("https://shop.one-shore.com/")
		print(self.driver.title)
		self.assertEqual(self.driver.title, "ONESHORE DEMO SHOP")

	def test_open_google(self):
		self.driver.get("https://google.com/")
		print(self.driver.title)
		self.assertEqual(self.driver.title, "Google")

	def tearDown(self):
		self.driver.quit()
