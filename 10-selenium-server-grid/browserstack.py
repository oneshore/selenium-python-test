# browserstack.py

import os
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
