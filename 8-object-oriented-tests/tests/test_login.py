import pytest
from types import SimpleNamespace
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait


from login_page import LoginPage
from home_page import HomePage

@pytest.fixture()
def loginPage(driver):
	return LoginPage(driver)

@pytest.fixture()
def homePage(driver):
	return HomePage(driver)

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
def test_login_success(loginPage, homePage:HomePage, account):
	print("__name__")
	print(account)
	
	loginPage.open()
	loginPage.enter_email_address(account.email)
	loginPage.enter_password(account.password)
	loginPage.click_login_button()

	assert homePage.logged_in()
	assert homePage.get_account_name() == account.full_name

@pytest.mark.failure
def test_login_failure(loginPage, homePage:HomePage, account):
	print("__name__")
	print(account)
	
	loginPage.open()
	loginPage.enter_email_address(account.email)
	loginPage.enter_password("invalid password")
	loginPage.click_login_button()

	assert loginPage.get_alert_text() == "Authentication failed."

	homePage.open()
	assert not homePage.logged_in()



