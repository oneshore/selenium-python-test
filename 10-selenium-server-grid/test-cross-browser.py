import pytest
from selenium import webdriver

SELENIUM_GRID_URL = "http://192.168.1.143:4444"



def test_on_chrome_linux():
	capabilities = { "platformName": "linux", "browserName": "chrome" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_safari_mac():
	capabilities = { "platformName": "macos", "browserName": "safari" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_firefox_mac():
	capabilities = { "platformName": "macos", "browserName": "firefox" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_edge_windows():
	capabilities = { "platformName": "win10", "browserName": "MicrosoftEdge"}
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

# pip install html-reporter
# pip install pytest-parallel
# pytest -vs --workers=4 --html-report=./report test-cross-browser.py
