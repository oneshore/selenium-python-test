import pytest
from webdriver_helpers import *
from random import randint

class TestCreateAccount:

	@pytest.fixture(autouse=True)
	def setup(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	def test_create_account(self):
		title = "Mrs."
		first_name = "Lucy"
		last_name = "O'brien"
		email = "lucy" + str(randint(1, 1000)) + "@example.com"
		password = "Password1!"

		self.navigate_to_create_account()
		self.select_social_title(title)
		self.enter_first_name(first_name)
		self.enter_last_name(last_name)
		self.enter_email(email)
		self.enter_password(password)

		self.check_required_checkboxes()
		sleep(2)
		self.check_required_checkboxes()
		sleep(2)
		self.click_save()
		sleep(2)

		assert self.logged_in()
		assert self.get_account_name() == first_name + " " + last_name

	def open_create_account_page(self):
		self.driver.get("https://shop.one-shore.com/index.php?controller=authentication&create_account=1")

	def navigate_to_create_account(self):
		self.driver.get("https://shop.one-shore.com")

		sign_in_button_locator = By.PARTIAL_LINK_TEXT, "Sign in"
		heading_locator = By.CSS_SELECTOR, "h1"
		create_account_button_locator = By.CSS_SELECTOR, ".no-account > a"

		self.driver.find_element(*sign_in_button_locator).click()
		heading = self.driver.find_element(*heading_locator).text
		assert heading == "Log in to your account"

		self.driver.find_element(*create_account_button_locator).click()
		heading = self.driver.find_element(*heading_locator).text
		assert heading == "Create an account"

	def select_social_title(self, title:str):
		title_locator = By.CSS_SELECTOR, ".radio-inline"
		for element in self.driver.find_elements(*title_locator):
			print(element.text)
			if element.text == title:
				element.click()

	def enter_first_name(self, firstname):
		first_name_field = self.driver.find_element(By.NAME, "firstname")
		first_name_field.send_keys(firstname)

	def enter_last_name(self, lastname):
		last_name_field = self.driver.find_element(By.NAME, "lastname")
		last_name_field.send_keys(lastname)

	def enter_email(self, email):
		email_field = self.driver.find_element(By.NAME, "email")
		email_field.send_keys(email)

	def enter_password(self, password):
		password_field = self.driver.find_element(By.NAME, "password")
		password_field.send_keys(password)

	def check_required_checkboxes(self):
		checkboxes_locator = By.XPATH, "//input[@type='checkbox']"
		checkboxes = self.driver.find_elements(*checkboxes_locator)

		print(f"checkboxes: {len(checkboxes)}")
		required_checkboxes = list(
			filter(lambda checkbox: checkbox.get_attribute("required"), checkboxes)
		)
		print(f"required_checkboxes: {len(required_checkboxes)}")
		[box.click() for box in required_checkboxes if not box.is_selected()]

	def click_save(self):
		save_button_locator = By.CSS_SELECTOR, ".register-form button[type=submit]"
		save_button = self.driver.find_element(*save_button_locator)
		self.scroll_into_view(save_button)

		sleep(4)
		save_button.click()


	def logged_in(self):
		self.wait.until(expected.title_is("ONESHORE DEMO SHOP"))
		user_info = self.driver.find_element(By.CSS_SELECTOR, ".user-info")
		if "Sign out" not in user_info.text:
			return False
		return True

	def get_account_name(self):
		return self.driver.find_element(By.CSS_SELECTOR, ".user-info .account").text

	def scroll_into_view(self, element):
		action:ActionChains = ActionChains(self.driver)
		action.move_to_element(element)
		action.perform()
