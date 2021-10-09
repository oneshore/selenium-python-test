from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

# options = EdgeOptions()
# options.use_chromium = True
#
# driver = Edge(options=options)

driver = webdriver.Chrome()
driver.get("https://shop.one-shore.com")

elem = driver.find_element_by_name("s")
# elem.clear()
elem.send_keys("mug")
elem.send_keys(Keys.RETURN)

element:WebElement = driver.find_elements_by_css_selector(".product-description")
len(element)

element.find_element_by_css_selector(".product-title")
element.find_element_by_css_selector(".price")

sleep(5)
driver.quit()
