WebDriver Wait
==============

Why wait?
---------

- Don't we want tests to be faster?
- Page Load
- Partial Page Load
- AJAX / Dynamic pages
- Single Page Apps
- Variable internet speed
- Makes it difficult to locate elements

Things to wait for
------------------

- Page to load
- Javascript to execute
- Elements to appear
- Elements to be within view
- Elements to be interactable (e.g. Clickable)


Inspecting elements
-------------------

element.is_displayed()
element.is_enabled()
element.is_selected()


Sleep
-----

- How to sleep?
```python
from time import sleep
sleep(1) # seconds
```
- Why not sleep?
- Performance may change
- Assume worst case scenario
- Alternatives?


Timeouts
--------

- Wait for page to load
```python
driver.set_page_load_timeout(30)
```
- Wait for javascript
```python
driver.set_script_timeout(60)
```

Implicit Wait
-------------

- Wait for element interaction
```python
driver.implicitly_wait(10)
```
- polls DOM every 300ms
- What's wrong with implicit waits?
- Still assumes worst case -- on element not found
- Same wait for everything


Explicit wait
-------------

- wait for a specific condition to occur
```python
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, timeout=10)
wait.until(expected_condition)
```

Expected Conditions
-------------------
- What do we wait for?
```python
from selenium.webdriver.support import expected_conditions as expected
expected.presence_of_element_located(locator) # locator is a tuple (by, text)
expected.visibility_of(element)
expected.element_to_be_clickable(locator)
expected.element_to_be_clickable(element)
- lots more expected conditions
```


Custom Wait Conditions
----------------------
- create a class with __call__() method
- returns False when condition doesn't match


Making Explicit waits nicer
---------------------------
_

- create a function (and add logging)
```python
def when_visible(locator, description="element", timeout=15):
	log(f"waiting for visibility of {description} located by {locator}")
	if not wait:
		wait = WebDriverWait(driver, timeout)
	return wait.until(expected.visibility_of_element_located(locator))

when_visible(logout_button).click()
```


References
----------

https://selenium-python.readthedocs.io/waits.html
https://www.selenium.dev/documentation/webdriver/waits/
