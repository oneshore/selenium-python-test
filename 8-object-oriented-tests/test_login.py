import pytest
from socket import gethostname
from time import sleep
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.common.by import By

account = SimpleNamespace(title='Mrs.',
		first_name='Tamara', last_name='Thomas', full_name='Tamara Thomas',
		email='nathan75@example.com', password='Password1!')

login_url = "https://shop.one-shore.com/index.php?controller=authentication"


def running_on_python_anywhere():
	if "console" in gethostname():
		return True
	return False

@pytest.fixture(autouse=True)
def chrome_options():
	chrome_options = webdriver.ChromeOptions()
	if running_on_python_anywhere():
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
	return chrome_options

@pytest.fixture()
def driver(chrome_options):
	print(chrome_options)
	driver = webdriver.Chrome(options=chrome_options)
	yield driver
	sleep(4)
	driver.quit()

def test_login(driver):
	driver.get(login_url)
	assert driver.title == "Login"
