from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://the-internet.herokuapp.com/dynamic_loading/2"
start = By.CSS_SELECTOR, "#start > button"
finish = By.CSS_SELECTOR, "#finish > h4"

try:
	driver = webdriver.Chrome()
	driver.get(url)

finally:
	sleep(3)
	driver.quit()
