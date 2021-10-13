import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
	driver = webdriver.Chrome()
	yield driver
	driver.quit()

def test_open_demo_shop(browser):
	browser.get("https://shop.one-shore.com")
	assert "ONE SHORE" in browser.title
