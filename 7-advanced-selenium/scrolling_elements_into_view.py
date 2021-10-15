from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

from typing import List, Tuple, Dict

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# scroll element into view

driver.get("https://shop.one-shore.com")
top_menu:WebElement = driver.find_element(By.ID, "top-menu")
top_menu.find_element(By.PARTIAL_LINK_TEXT, "ACCESSORIES").click()
items:List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "article")
for item in items:
	print(item.text)
	action:ActionChains = ActionChains(driver)
	action.move_to_element(item)
	action.perform()
	sleep(2)


# alternative using javascript only
for item in items:
	driver.execute_script("arguments[0].scrollIntoView();", item)
