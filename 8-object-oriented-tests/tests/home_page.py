from webdriver_helpers import *
from selenium_page import SeleniumPage

class HomePage(SeleniumPage):

	TITLE = "ONESHORE DEMO SHOP"
	URL = "https://shop.one-shore.com/index.php"

	sign_in_link_locator = By.PARTIAL_LINK_TEXT, "Sign in"
	sign_out_link_locator = By.CSS_SELECTOR, ".user-info a.logout"
	account_link_locator = By.CSS_SELECTOR, ".user-info a.account"
	user_info_link_locator = By.CSS_SELECTOR, ".user-info > a:first-of-type"

	def __init__(self, driver:WebDriver):
		super().__init__(driver, self.URL)

	def open(self):
		self.driver.get(HomePage.URL)

	def is_current_page(self):
		try:
			self.wait.until(expected.title_is(self.TITLE))
			return True
		except:
			print(f"not on expected page {__class__.__name__}")
			return False

	def logged_in(self):
		try:
			if not self.is_current_page():
				raise Exception(f"not on expected page {__class__.__name__}")

			user_info = self.driver.find_element(*self.user_info_link_locator)
			print("user info: " + user_info.text)
			
			if "Sign out" in user_info.text:
				print("logged in")
				return True
			else:
				print("logged out")
				return False
		except TimeoutException as e: 
			print("timeout")
			print(e)
			return False
		except Exception as e:
			print(e)
		return False

		
	def get_account_link(self):
		account_link =  self.driver.find_element(*HomePage.account_link_locator)
		print(account_link.text)
		return account_link

	def get_account_name(self):
		return self.get_account_link().text

	def click_account_link(self):
		self.get_account_link().click()