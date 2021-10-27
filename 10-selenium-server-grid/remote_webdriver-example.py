from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# selenium server 3 path
selenium_server_url = "http://localhost:4444/wd/hub"

# selenium server 4 path
selenium_server_url = "http://localhost:4444"

capabilities = { "browserName" : "chrome" }
capabilities = { "browserName" : "firefox" }
capabilities = { "browserName": "MicrosoftEdge" }

capabilities = DesiredCapabilities.CHROME
capabilities = DesiredCapabilities.FIREFOX
capabilities = DesiredCapabilities.EDGE
capabilities = DesiredCapabilities.SAFARI

driver = webdriver.Remote(command_executor=selenium_server_url, desired_capabilities=capabilities)
driver.get("https://shop.one-shore.com")
print(driver.title)
driver.quit()
