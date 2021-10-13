import pytest
from selenium import webdriver
from time import sleep

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_page(browser):
	if browser == "chrome":
		driver = webdriver.Chrome()
	if browser == "firefox":
		driver = webdriver.Firefox()

	driver.maximize_window()
	driver.get("https://google.com")
	print(driver.capabilities['browserName'], driver.title)

	sleep(3)
	driver.quit()
