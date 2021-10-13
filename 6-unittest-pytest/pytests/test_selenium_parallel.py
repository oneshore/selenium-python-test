import pytest

from selenium import webdriver

import pytest
from selenium import webdriver
from time import sleep

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_google(browser):
	if browser == "chrome":
		driver = webdriver.Chrome()
		driver.set_window_size(600, 600)
		driver.set_window_position(0,0)
	if browser == "firefox":
		driver = webdriver.Firefox()
		driver.set_window_size(600, 600)
		driver.set_window_position(0,600)

	driver.get("https://google.com")
	print(driver.capabilities['browserName'], driver.title)

	sleep(5)
	driver.quit()

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_shop(browser):
	if browser == "chrome":
		driver = webdriver.Chrome()
		driver.set_window_size(600, 600)
		driver.set_window_position(600,0)
	if browser == "firefox":
		driver = webdriver.Firefox()
		driver.set_window_size(600, 600)
		driver.set_window_position(600,600)

	driver.get("https://shop.one-shore.com")
	print(driver.capabilities['browserName'], driver.title)

	sleep(5)
	driver.quit()
