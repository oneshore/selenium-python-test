1. Start Selenium Server

	`java -jar selenium-server-standalone-3.141.59.jar`

2. Run selenium with remote web driver and desired capabilities

```python
# selenium-server-example.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_server_url = "http://localhost:4444/wd/hub"
capabilities = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=selenium_server_url, desired_capabilities=capabilities)
driver.get("https://one-shore.com")
sleep(3)
driver.quit()
```

3. Start Selenium Grid hub

	`java -jar selenium-server-4.0.0.jar hub`

4. Start Selenium Grid node

	`java -jar selenium-server-4.0.0.jar node --hub http://192.168.1.143:4444`

5. Run on selenium grid

```python
# grid-example.py

from selenium import webdriver
from selenium.webdriver.common import desired_capabilities

# selenium server 3 path
selenium_server_url = "http://localhost:4444/wd/hub"

# selenium server 4 path
selenium_server_url = "http://localhost:4444"

capabilities = { "browserName" : "MicrosoftEdge", "platformName" : "Win10" }
driver = webdriver.Remote(command_executor=selenium_server_url, desired_capabilities=capabilities)
driver.get("https://shop.one-shore.com")
print(driver.title)
driver.quit()
```


6. Test Cross Browser

```python
#test-cross-browser.py

import pytest
from selenium import webdriver

SELENIUM_GRID_URL = "http://192.168.1.143:4444"

def test_on_chrome_linux():
	capabilities = { "platformName": "linux", "browserName": "chrome" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_safari_mac():
	capabilities = { "platformName": "macos", "browserName": "safari" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_firefox_mac():
	capabilities = { "platformName": "macos", "browserName": "firefox" }
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()

def test_on_edge_windows():
	capabilities = { "platformName": "win10", "browserName": "MicrosoftEdge"}
	driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)
	driver.get("https://shop.one-shore.com")
	print(driver.title, driver.capabilities)
	driver.quit()
```

7. Execute tests in parallel

	`pip install pytest-xdist`

	`pip install pytest-html`

	`pip install pytest-parallel`

	`pytest -vs -n 4 --html=report.html --self-contained-html test-cross-browser.py`

8. Alternatives

	`pip install pytest-parallel`

	`pip install pytest-html-reporter`

	`pytest -vs --workers=4 --html=report.html --self-contained-html test-cross-browser.py`

	`pytest -vs --html-report=./reports test-cross-browser.py`

	### NOTE:  pytest-html-reporter does not report parallel parameterized tests

9. Run cross browser with parametrize

```python
# test-with-parametrize.py

import pytest
from time import sleep
from selenium import webdriver

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
	driver.quit()
```
10. Run parameterized tests in parallel

	`pytest -vs -n 6 --html=./report.html test-with-parametrize.py`
