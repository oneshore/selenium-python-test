import pytest

users = {
	'valid_user': {
		'email' : 'test@one-shore.com',
		'password' : 'Password1!'
	},
	'invalid_password': {
		'email' : 'test@one-shore.com',
		'password': 'Password2!'
	}
}

from selenium import webdriver

def credentials(param):
	print(f"{__name__} : {param}")
	yield users.get(param)
	print("done")

@pytest.fixture(params = ['valid_user', 'invalid_password'])
def login_fixture(param):
	print(f"{__name__} : {param}")
	driver = webdriver.Chrome()
	driver.get("https://shop.one-shore.com")
	driver.find_element_by_link_text("Sign in")
	yield from credentials(param)

	driver.

@pytest.mark.parametrize("credentials", )
def test_login():
