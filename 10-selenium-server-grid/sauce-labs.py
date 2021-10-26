import os
from selenium import webdriver

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
SAUCE_URL = f"https://ondemand.us-west-1.saucelabs.com/wd/hub"

SAUCE_OPTIONS = {
	"username": SAUCE_USERNAME,
	"accessKey": SAUCE_ACCESS_KEY,
	"name": "Options test"
}

options = {
	"browserName": "chrome",
	"version": "latest",
	"platform": "any",
	"sauce:options": SAUCE_OPTIONS
}

print(options)

driver = webdriver.Remote(command_executor=SAUCE_URL, desired_capabilities=options)
driver.get("https://shop.one-shore.com")
print(driver.title)
driver.quit()
