from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/dynamic_loading/2"
start = By.CSS_SELECTOR, "#start > button"
finish = By.CSS_SELECTOR, "#finish > h4"

try:
	driver = webdriver.Chrome()
finally:
	driver.quit()
