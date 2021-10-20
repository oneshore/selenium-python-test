import pytest
from time import sleep
from types import SimpleNamespace
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException


@pytest.fixture()
def account():
	account = SimpleNamespace(
		title='Mrs.',
		first_name='Tamara',
		last_name='Thomas',
		full_name='Tamara Thomas',
		email='nathan75@example.com',
		password='Password1!')

	return account

login_url = "https://shop.one-shore.com/index.php?controller=authentication"
email_field_locator = By.CSS_SELECTOR, "#login-form input[name=email]"
password_field_locator = By.CSS_SELECTOR, "#login-form input[name=password]"
login_button = By.CSS_SELECTOR, "#login-form button#submit-login"

@pytest.mark.success
def test_login_success(driver, account):
	print("__name__")
	driver.get(login_url)
	print("got title: " + driver.title)
	assert driver.title == "Login"
	print(account)
	driver.find_element(*email_field_locator).send_keys(account.email)
	driver.find_element(*password_field_locator).send_keys(account.password)
	driver.find_element(*login_button).click()
	print("got title: " + driver.title)
	assert logged_in(driver)
	assert get_account_name(driver) == account.full_name


@pytest.mark.failure
def test_login_failure(driver, account):
	print("__name__")
	driver.get(login_url)
	assert driver.title == "Login"
	print("got title: " + driver.title)
	print(account)
	driver.find_element(*email_field_locator).send_keys(account.email)
	driver.find_element(*password_field_locator).send_keys("invalid password")
	driver.find_element(*login_button).click()
	print("got title: " + driver.title)
	assert not logged_in(driver)

def logged_in(driver):
	try: 
		wait = WebDriverWait(driver, 10)
		wait.until(expected.title_is("ONESHORE DEMO SHOP"))
		user_info = driver.find_element(By.CSS_SELECTOR, ".user-info")
		print("user info: " + user_info.text)
		if "Sign out" in user_info.text:
			print("logged in")
			return True
		else:
			return False
	except TimeoutException as e: 
		print("timeout")
		print(e)
		return False
	except  WebDriverException as e:
		print(e)
		return False

	
def get_account_name(driver):
	account_name =  driver.find_element(By.CSS_SELECTOR, ".user-info .account").text
	print(account_name)
	return account_name