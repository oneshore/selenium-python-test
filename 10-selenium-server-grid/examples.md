1. Start Selenium Server

	`java -jar selenium-server-standalone-3.141.59.jar`
	`java -jar selenium-server-4.0.0.jar standalone -port 6666`

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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

11. Run tests on Sauce Labs

On Mac or Linux

	`export SAUCE_USENRAME=yourusername`
	`export SAUCE_ACCESS_KEY=youraccesskey`

On Windows

`setx SAUCE_USENRAME yourusername`
`setx SAUCE_ACCESS_KEY youraccesskey`

```python
import os
from selenium import webdriver

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

SAUCE_OPTIONS = {
	"username": SAUCE_USERNAME,
	"accessKey": SAUCE_ACCESS_KEY,
	"name": "Shop test"
}

capabilities = {
	"browserName": "chrome",
	"version": "latest",
	"platform": "any",
	"sauce:options": SAUCE_OPTIONS
}

driver = webdriver.Remote(command_executor=SAUCE_URL, desired_capabilities=capabilities)
driver.get("https://shop.one-shore.com")
print(driver.title)
driver.quit()
```

12. Run tests on Browserstack


```python
# browserstack-example.py

import os
from selenium import webdriver

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

capabilities = {
	"browser": "Safari",
	"browser_version": "latest",
	"os": "OS X",
	"os_version": "Big Sur",
	"name": "Test Name"
}

driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=capabilities)
driver.get("https://shop.one-shore.com")
print(driver.title)
driver.quit()
```
