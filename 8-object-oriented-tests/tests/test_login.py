import pytest
from time import sleep
from types import SimpleNamespace
from selenium.webdriver.common.by import By


login_url = "https://shop.one-shore.com/index.php?controller=authentication"

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

def test_login(driver, account):
	driver.get(login_url)
	assert driver.title == "Login"
	print(account)
