import os
from time import sleep
from typing import List, Tuple, Dict

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def driver():
	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	driver.maximize_window()
	yield driver
	sleep(3)
	driver.quit()

@pytest.mark.navigate
def test_navigate_to_create_account(driver:WebDriver):
	""" navigate to create account page """
	driver.get("https://shop.one-shore.com")
	driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
	wait = WebDriverWait(driver, 10)
	create_account_locator = (By.CSS_SELECTOR, ".no-account a")
	wait.until(expected.element_to_be_clickable(create_account_locator)).click()

	create_account_form_locator = By.CSS_SELECTOR, ".register-form form"
	create_account_form = wait.until(expected.visibility_of_element_located(create_account_form_locator))
	assert create_account_form.is_displayed()


def test_create_account(driver:WebDriver):
	""" create account """
	create_account_url = "https://shop.one-shore.com/index.php?controller=authentication&create_account=1"

	driver.get(create_account_url)
	select_social_title("Mrs.")
	enter_first_name("Lucy")
	enter_last_name("O'hara")
	enter_email("lucyo@example.com")
	enter_password("Password1!")
	check_required_boxes()
	click_save_button()

	wait = WebDriverWait(driver, 10)
	wait.until(expected.url_changes)

	user_info = driver.find_element(By.CSS_SELECTOR, ".user-info")
	assert "Sign out" in user_info.text
	assert "Lucy O'hara" in user_info.text

##### select title (radio button)
def select_social_title(text):
	titles_locator = By.CSS_SELECTOR, ".radio-inline"
	titles_visible = expected.presence_of_all_elements_located(titles_locator)
	wait = WebDriverWait(driver, 10)
	titles = wait.until(titles_visible)
	for title in titles:
		print(title.text)
		if title.text == text:
			title.click()

def enter_first_name(firstname):
	first_name_field = driver.find_element(By.NAME, "firstname")
	first_name_field.send_keys(firstname)

def enter_last_name(lastname):
	last_name_field = driver.find_element(By.NAME, "lastname")
	last_name_field.send_keys(lastname)

def enter_email(email):
	email_field = driver.find_element(By.NAME, "email")
	email_field.send_keys(email)

def enter_password(password):
	password_field = driver.find_element(By.NAME, "password")
	password_field.send_keys("Password1!")

def check_required_boxes():
	checkbox_locator = By.CSS_SELECTOR, ".register-form input[type=checkbox]"
	checkboxes = driver.find_elements(*checkbox_locator)
	required_checkboxes = list(filter(lambda checkbox: checkbox.get_attribute("required"), checkboxes))
	[checkbox.click() for checkbox in required_checkboxes if not checkbox.is_selected()]

def click_save_button():
	save_button_locator = By.CSS_SELECTOR, ".register-form button[type=submit]"
	driver.find_element(*save_button_locator).click()
