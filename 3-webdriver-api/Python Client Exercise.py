# Python Client Exercise
## Go to the Demo shop website and interact with it using Selenium


from selenium.webdriver.remote.webelement import WebElement


try:

### Import Selenium webdriver module

	from selenium import webdriver

### Launch the browser

	driver = webdriver.Chrome()

### Inspect the browser properties

	driver.name
	driver.session_id
	driver.capabilities

### Window size and position

	driver.get_window_size()
	driver.get_window_position()
	driver.get_window_rect() # size and position
	driver.minimize_window()
	driver.maximize_window()


### Open the site

	url = "https://shop.one-shore.com"

	driver.get(url)

### Inspect the page properties

	driver.title
	driver.current_url
	driver.page_source

### Navigate

	driver.back()
	driver.forward()
	driver.refresh()

### close and quit

	driver.close()
	driver.quit()

### Find Element

	driver.find_element_by_id("contact-link")
	driver.find_element_by_tag_name("a") # first link is the contact us link

	driver.find_element_by_name("s") # search field
	driver.find_element_by_tag_name("button") # search button

	driver.find_element_by_link_text("Contact us")
	driver.find_element_by_partial_link_text("Contact")

	driver.find_element_by_class_name("product-description")
	driver.find_element_by_css_selector(".product-description")
	driver.find_element_by_xpath("//.product-description")


### Find Elements

	driver.find_elements_by_tag_name("a")

	driver.find_element_by_class_name("product-description")
	driver.find_elements_by_css_selector(".product-title")

	for element in driver.find_elements_by_css_selector(".product-description"):
		print(element.text)


### Inspecting element properties

### Interacting with Elements



### Find elements from a Web Element

	element:WebElement = driver.find_elements_by_css_selector(".product-description")
	element.find_element_by_css_selector(".product-title")
	element.find_element_by_css_selector(".price")

finally:
	driver.quit()
