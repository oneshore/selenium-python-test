from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_server_url = "http://localhost:4444/wd/hub"
capabilities = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=selenium_server_url, desired_capabilities=capabilities)
driver.get("https://one-shore.com")
sleep(3)
driver.quit()
