import pytest
import sys
import logging
from webdriver_helpers import *
from selenium_page import SeleniumPage

class LoginForm:
	email_field_locator = By.CSS_SELECTOR, "#login-form input[name=email]"
	password_field_locator = By.CSS_SELECTOR, "#login-form input[name=password]"
	login_button_locator = By.CSS_SELECTOR, "#login-form button#submit-login"

class NewsletterForm:
	email_field_locator = By.CSS_SELECTOR, ".block_newsletter input[name=email]"
	subscribe_button_locator = By.CSS_SELECTOR, ".block_newsletter input[type=submit][value=Subscribe]"
	
class LoginPage(SeleniumPage):
	alert_block = By.CSS_SELECTOR, ".help-block .alert"

	URL = "https://shop.one-shore.com/index.php?controller=authentication"
	TITLE = "Login"

	def __init__(self, driver:WebDriver):
		super().__init__(driver, self.URL)

	def enter_email_address(self, email_address):
		email_field = self.driver.find_element(*LoginForm.email_field_locator)
		email_field.send_keys(email_address)
		self.log.debug(f"entered email address: {email_address}")

	def enter_password(self, password):
		password_field = self.driver.find_element(*LoginForm.password_field_locator)
		password_field.send_keys(password)
		self.log.debug(f"entered password: {password}")

	def click_login_button(self):
		login_button = self.driver.find_element(*LoginForm.login_button_locator)
		login_button.click()
		self.log.debug(f"clicked login button")

	def get_alert_text(self):
		alert = self.wait.until(expected.visibility_of_element_located(LoginPage.alert_block))
		return alert.text

	def login(self, email_address, password):
		if not self.is_current_page():
			self.open()
		self.enter_email_address(email_address)
		self.enter_password(password)
		self.click_login_button()
