import pytest
from webdriver_helpers import *

# class LoginForm:
# 	email_field_locator = By.CSS_SELECTOR, "#login-form input[name=email]"
# 	password_field_locator = By.CSS_SELECTOR, "#login-form input[name=password]"
# 	login_button_locator = By.CSS_SELECTOR, "#login-form button#submit-login"

# class NewsletterForm:
# 	email_field_locator = By.CSS_SELECTOR, ".block_newsletter input[name=email]"
# 	subscribe_button_locator = By.CSS_SELECTOR, ".block_newsletter input[type=submit][value=Subscribe]"
	
class LoginPage:
	email_field_locator = By.CSS_SELECTOR, "#login-form input[name=email]"
	password_field_locator = By.CSS_SELECTOR, "#login-form input[name=password]"
	login_button_locator = By.CSS_SELECTOR, "#login-form button#submit-login"

	alert_block = By.CSS_SELECTOR, ".help-block .alert"

	URL = "https://shop.one-shore.com/index.php?controller=authentication"
	
	def __init__(self, driver:WebDriver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
	
	def open(self):
		self.driver.get(LoginPage.URL)
		print(f"opened Login Page at {self.driver.current_url} with title: {self.driver.title}")

	def enter_email_address(self, email_address):
		email_field = self.driver.find_element(*LoginPage.email_field_locator)
		email_field.send_keys(email_address)
		print(f"entered email address: {email_address}")

	def enter_password(self, password):
		password_field = self.driver.find_element(*LoginPage.password_field_locator)
		password_field.send_keys(password)
		print(f"entered password: {password}")


	def click_login_button(self):
		login_button = self.driver.find_element(*LoginPage.login_button_locator)
		login_button.click()
		print(f"clicked login button")

	def get_alert_text(self):
		alert = self.wait.until(expected.visibility_of_element_located(LoginPage.alert_block))
		return alert.text

