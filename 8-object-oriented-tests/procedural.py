from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def search_for_mug():
	driver.get("https://shop.one-shore.com")
	assert driver.title == "ONESHORE DEMO SHOP"
	driver.find_element(By.NAME, "s").send_keys("mug")
	driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


driver.quit()
