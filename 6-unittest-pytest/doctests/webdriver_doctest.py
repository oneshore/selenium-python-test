from selenium import webdriver

def open_demo_shop():
	"""
		Launches webdriver and navigates to the demo shop
		>>> open_demo_shop()
		'ONESHORE DEMO SHOP'
	"""

	try:
		driver = webdriver.Chrome()
		driver.get("https://shop.one-shore.com")
		return driver.title
	except Exception as e:
		print(e)
	finally:
		driver.quit()



if __name__ == "__main__":
	import doctest
	doctest.testmod()
	# doctest.testfile()
