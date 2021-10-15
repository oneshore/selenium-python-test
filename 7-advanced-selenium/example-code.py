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
	action:ActionChains = ActionChains(driver)
	action.move_to_element(item)
	action.perform()
	driver.execute_script("arguments[0].scrollIntoView();", item)

	sleep(2)


driver.f
### filtering with for loop
#### create account

driver.get("https://shop.one-shore.com")
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
wait = WebDriverWait(driver, 10)
create_account_locator = (By.CSS_SELECTOR, ".no-account a")
wait.until(expected.element_to_be_clickable(create_account_locator)).click()

##### shortcut to create account

driver.get("https://shop.one-shore.com/index.php?controller=authentication&create_account=1")

##### select title (radio button)
def select_social_title(text):
	titles_locator = By.CSS_SELECTOR, ".radio-inline"
	titles_visible = expected.presence_of_all_elements_located(titles_locator)
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
	checkboxes = driver.find_elements(By.CSS_SELECTOR)
# filtering with lambda expression

# filtering with list comprehension

driver.get("https://shop.one-shore.com")

items:List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "article")

element = [element for element in elements]

# check if checkbox is clicked
checkbox_locator = By.CSS_SELECTOR, ".register-form input[type=checkbox]"
checkboxes = driver.find_elements(*checkbox_locator)
required_checkboxes = list(filter(lambda checkbox: checkbox.get_attribute("required"), checkboxes))
for checkbox in required_checkboxes:
	checkbox.click()
	# doesn't check
	if not checkbox.is_selected():
		checkbox.click()

[checkbox.click() for checkbox in required_checkboxes if not checkbox.is_selected()]

checked_checkboxes = [checkbox.is_selected() in ]

# check if radiobox selected

# select & multiselect
### Contact Form

contact_url = "https://shop.one-shore.com/index.php?controller=contact"
driver.get(contact_url)

from selenium.webdriver.support.ui import Select
subject_dropdown = driver.find_element(By.CSS_SELECTOR, ".contact-form select[name=id_contact]")
select = Select(subject_dropdown)
select.select_by_index(1)
select.select_by_value("2")
select.select_by_visible_text("Webmaster")


# alert / confirm / prompt

# switch to window / frame

# http basic & digest auth

# file upload
