import pytest
from types import SimpleNamespace
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

from login_page import LoginPage

@pytest.fixture()
def loginPage(driver):
	return LoginPage(driver)

@pytest.fixture()
def account():
	account = SimpleNamespace(
		title='Mrs.',
		first_name='Tamara',
		last_name='Thomas',
		full_name='Tamara Thomas',
		email='tamarathomas@example.com',
		password='Password1!')

	return account


@pytest.mark.success
def test_login_success(loginPage, account):
	print("__name__")
	print(account)
	
	loginPage.open()
	loginPage.enter_email_address(account.email)
	loginPage.enter_password(account.password)
	loginPage.click_login_button()

	assert logged_in(loginPage.driver)
	assert get_account_name(loginPage.driver) == account.full_name

@pytest.mark.failure
def test_login_failure(driver, account):
	print("__name__")
	print(driver)
	print(account)
	
	login_page = LoginPage(driver)
	login_page.open()
	login_page.enter_email_address(account.email)
	login_page.enter_password("invalid password")
	login_page.click_login_button()

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