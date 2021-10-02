from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(options=chrome_options)

try:
	browser.get("https://www.google.com")

	print(f"got page title: {browser.title}")
	print(f"got page url: {browser.current_url}")
	print(f"got page source: {browser.page_source}")

	print(f"got window size: {browser.get_window_size()}")
	print(f"got window position: {browser.get_window_position()}")
	print(f"got window rectangle (size & position): {browser.get_window_rect()}")

finally:
	sleep(3)
	browser.quit()
