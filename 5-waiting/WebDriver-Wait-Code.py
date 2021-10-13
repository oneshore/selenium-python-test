#WebDriver-Wait-Code.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()

# timeouts
driver.set_page_load_timeout(30)
driver.set_script_timeout(60)

# raises TimeoutException

# check for conditions
element:WebElement = driver.find_element(By.ID, "id")

element.is_displayed()
element.is_enabled()
element.is_selected()


# sleep
from time import sleep
sleep(1) # seconds

# implicitly wait
driver.implicitly_wait(10)

# explicitly wait
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, timeout=10)
wait.until(condition)

# expected conditions
from selenium.webdriver.support import expected_conditions as expected
expected.presence_of_element_located(locator)
expected.visibility_of_element_located(locator) # locator is a tuple (By, text)
expected.visibility_of(element)
expected.element_to_be_clickable(locator)
expected.element_to_be_clickable(element)

# multiple elements
expected.presence_of_all_elements_located(locator)
expected.visibility_of_all_elements_located(locator)
expected.visibility_of_any_elements_located(locator)

# selected
expected.element_to_be_selected(element)
expected.element_located_to_be_selected(locator)
expected.element_selection_state_to_be(element, True)
expected.element_located_selection_state_to_be(locator, False)

# alerts
expected.alert_is_present()

# windows and frames
expected.new_window_is_opened(current_window_handles)
expected.number_of_windows_to_be(2)
expected.frame_to_be_available_and_switch_to_it(frame_id)

# text and attributes
expected.text_to_be_present_in_element(locator, "text")
expected.text_to_be_present_in_element_value(locator, "value")

# title and url
expected.title_is("title")
expected.title_contains("part of title")
expected.url_to_be("url")
expected.url_contains("part of url")
expected.url_changes("current url")
expected.url_matches(pattern)

# element is no longer available (e.g. on new page)
expected.staleness_of(element)

# negative
expected.invisibility_of_element(element)
expected.invisibility_of_element_located(locator)
wait.until_not(condition)

# custom wait
class not_empty(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.get_attribute("value"):
            return element
        else:
            return False

search_field_locator = By.NAME, "s"
wait.until(not_empty(search_field_locator))

# cleanup waits
from selenium.webdriver.support import expected_conditions
expected = expected_conditions
visible = expected.visibility_of_element_located
when = wait.until
logout_button = By.LINK_TEXT, "Log out"

when(visible(logout_button)).click()


# wait function
def when_visible(locator, description="element", timeout=15):
	print(f"waiting for visibility of {description} located by {locator}")
	if not wait:
		wait = WebDriverWait(driver, timeout)
	return wait.until(expected.visibility_of_element_located(locator))

when_visible(logout_button).click()

# wrap actions
def click(locator):
	wait.until(expected_conditions.element_to_be_clickable(locator)).click()
