from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from time import sleep
from socket import gethostname

url = "https://the-internet.herokuapp.com/dynamic_loading/2"
start = By.CSS_SELECTOR, "#start > button"
finish = By.CSS_SELECTOR, "#finish > h4"

options = webdriver.ChromeOptions()
if "console" in gethostname():
	options.add_argument("--headless")
	options.add_argument("--disable-gpu")

try:

	driver = webdriver.Chrome(options=options)
	driver.get(url)
	sleep(3)
	driver.find_element(*start).click()

	wait = WebDriverWait(driver, 10)
	element = wait.until(expected.visibility_of_element_located(finish))
	print("text: " + element.text)
finally:
	sleep(3)
	driver.quit()
