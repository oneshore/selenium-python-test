import pytest
from time import sleep
from selenium import webdriver
from pytest_html_reporter import attach

SELENIUM_GRID_URL = "http://192.168.1.143:4444"

platforms = [
	("chrome", "macos"),
	("safari", "macos"),
	("firefox", "macos"),
	("chrome", "linux"),
	("chrome", "windows"),
	("MicrosoftEdge", "windows")
]

@pytest.mark.parametrize("browser,platform", platforms)
def test_cross_browser(browser, platform):
	capabilities = { "browserName": browser, "platformName": platform }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, capabilities)
	attach(data=driver.get_screenshot_as_png())
	driver.quit()
