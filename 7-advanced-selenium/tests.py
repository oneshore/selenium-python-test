import pytest

from time import sleep
from typing import List, Tuple, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

present = expected.presence_of_element_located
visible = expected.visibility_of_element_located
clickable = expected.element_to_be_clickable
all_present = expected.presence_of_all_elements_located
text_present = expected.text_to_be_present_in_element

driver = webdriver.Chrome()

@pytest.fixture()
def driver():
	driver:WebDriver = webdriver.Chrome()
	driver.get("https://shop.one-shore.com")
	yield driver
	sleep(2)
	driver.quit()


def search(text:str):
    search = driver.find_element("id", "search_widget")
    search_field = search.find_element("name", "s")
    search_field.clear()
    search_field.send_keys(text)
    search_button = search.find_element("xpath", "//button[@type='submit']")
    search_button.click()
    wait = WebDriverWait(driver, 10)
    breadcrumbs = By.CSS_SELECTOR, ".breadcrumb"

    search_results_present = text_present(breadcrumbs, "Search results")
    wait.until(search_results_present)




def test_search_for_customizable_mug(driver:WebDriver):
	search_field = driver.find_element_by_name("s")
	search_field.clear()
	search_field.send_keys("mug")
	search_button = driver.find_element_by_xpath("//button[@type='submit']")
	search_button.click()
	wait = WebDriverWait(driver, 10)
	breadcrumbs = By.CSS_SELECTOR, ".breadcrumb"
	search_results_present = expected.text_to_be_present_in_element(breadcrumbs, "Search results")
	wait.until(search_results_present)


def search_for_item(item:str):



