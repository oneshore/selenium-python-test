# samples.py
from selenium import webdriver
driver = webdriver.Chrome()

#import by
from selenium.webdriver.common.by import By

# find element with explicit locator type
driver.find_element_by_id("my-id")
driver.find_element_by_tag_name("div")

# find element with locator arguments
driver.find_element(By.ID, "my-id")
driver.find_element(By.NAME, "my-name")
driver.find_element(By.CLASS_NAME, "my-class")

# webdriver and webelement both implement search context
element = driver.find_element(By.ID, "my-id")
nested_element = element.find_element(By.TAG_NAME, "a")

# saving a locator as a tuple
my_locator = By.CSS_SELECTOR, "#my-id > div[name=my-name]"
type(my_locator) # tuple

# find_element() takes two arguments
driver.find_element(By.CSS_SELECTOR, ".product-description")

# unpack the tuple with * operator (not multiplication)
driver.find_element(*my_locator)
