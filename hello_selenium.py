from selenium import webdriver

browser = webdriver.Chrome()

try:
	browser.get("https://www.google.com")
	print("Page title was '{}'".format(browser.title))

finally:
	browser.quit()
