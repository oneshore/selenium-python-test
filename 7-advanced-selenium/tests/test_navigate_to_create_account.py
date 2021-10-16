import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.navigate
def test_navigate_to_create_account(driver):
	driver.get("https://shop.one-shore.com")

	sign_in_button_locator = By.PARTIAL_LINK_TEXT, "Sign in"
	heading_locator = By.CSS_SELECTOR, "h1"
	create_account_button_locator = By.CSS_SELECTOR, ".no-account > a"

	driver.find_element(*sign_in_button_locator).click()
	heading = driver.find_element(*heading_locator).text
	assert heading == "Log in to your account"

	driver.find_element(*create_account_button_locator).click()
	heading = driver.find_element(*heading_locator).text
	assert heading == "Create an account"
