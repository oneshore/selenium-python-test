from selenium import webdriver
from time import sleep

def test_safari():
	driver = webdriver.Safari()
	driver.get("https://shop.one-shore.com")
	sleep(2)
	driver.quit()
