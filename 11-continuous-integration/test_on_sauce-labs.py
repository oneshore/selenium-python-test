import os
import pytest

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

### add username and access key to URL

# SAUCE_URL = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.us-west-1.saucelabs.com/wd/hub"
# capabilities = {
# 	"browserName": "chrome",
# 	"version": "",
# 	"platform": "any",
# 	"name": "Test name"
# }
# driver = webdriver.Remote(command_executor=SAUCE_URL, desired_capabilities=capabilities)

### include username and access key to sauce:options in capabilities
SAUCE_URL = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

SAUCE_OPTIONS = {
	"username": SAUCE_USERNAME,
	"accessKey": SAUCE_ACCESS_KEY,
	"name": "Shop test"
}


@pytest.fixture
def driver(request):
	testname = request.node.name
	SAUCE_OPTIONS['name'] = testname

	capabilities = {
		"browserName": "chrome",
		"version": "latest",
		"platform": "any",
		"sauce:options": SAUCE_OPTIONS
	}

	driver = webdriver.Remote(command_executor=SAUCE_URL, desired_capabilities=capabilities)
	print(f"SauceOnDemandSessionID={driver.session_id} job-name={__name__}")
	yield driver
	driver.quit()

def test_open_shop(driver):
	driver.get("https://shop.one-shore.com")
	print(driver.title)
	assert driver.title == "ONESHORE DEMO SHOP"

def test_contact_form_on_sauce(driver):
	driver.get("https://shop.one-shore.com")
	print(driver.title)

	wait = WebDriverWait(driver, 10)

	### navigate to contact page
	contact_url = "https://shop.one-shore.com/index.php?controller=contact"
	driver.get(contact_url)

	### select subject
	subject_dropdown_locator = By.CSS_SELECTOR, ".contact-form select[name=id_contact]"
	subject_dropdown = wait.until(expected.element_to_be_clickable(subject_dropdown_locator))
	select = Select(subject_dropdown)
	select.select_by_visible_text("Webmaster") # parameterize

	# ### alternatives
	# select.select_by_index(1)
	# select.select_by_value("2")

	### enter email address
	email_locator = By.CSS_SELECTOR, ".contact-form input[type=email]" # need to be specific
	email_field = driver.find_element(*email_locator)
	email_field.send_keys("email@example.com") # parameterize

	# ### set file attachment
	# file_path = os.path.abspath("logo.png")
	# attachment_locator = By.CSS_SELECTOR, ".contact-form input[type=file]"
	# attachment_field = driver.find_element(*attachment_locator)
	# attachment_field.send_keys(file_path)


	### type message
	message = "Awesome website!"
	message_field_locator = By.CSS_SELECTOR, ".contact-form textarea[name=message]"
	message_field = driver.find_element(*message_field_locator)
	message_field.send_keys(message)

	### click Send button
	send_button_locator = By.CSS_SELECTOR, ".contact-form input[type=submit][value=Send]"
	driver.find_element(*send_button_locator).click()

	### verify sent
	alert_message_locator = By.CSS_SELECTOR, ".contact-form .alert"
	alert_message = wait.until(expected.visibility_of_element_located(alert_message_locator))
	assert alert_message.text == "Your message has been successfully sent to our team."
