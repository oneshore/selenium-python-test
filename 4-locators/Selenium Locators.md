Selenium Locators
=================

What is a Locator
-----------------

- Finding elements in Selenium is nearly half the job
- Waiting for elements to be in the right state is nearly the other half (more on that tomorrow)
- 80/20 rule (Pareto Principle) : 80% of results come from 20% of actions
- Locators tell selenium (and the browser) (and javascript) how to find elements on the DOM

HTML DOM
--------

- HTML Documents have "tree" structure
- HTML Elements: parent, children, siblings
- Tag, attributes, text nodes
- "DOM" is the HTML Document Object Model - hierarchy of elements on the page
- Allows you to programmatically manipulate elements on the page
- Javascript uses:
	```javascript
		document.getElementById("my-id")
		document.getElementsByTagName("div")
		document.getElementsByName("my-name")
		document.getElementsByClassName("my-class")
	```
- Javascript also has query selector (based on JQuery) that use :
	```javascript
		document.querySelector(".product-description > .product-title a")
	```
- Javascript XPATH selector is ugly (but can be wrapped in a simple function):
	```javascript
		function getElementByXpath(path) {
			return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
		}
	```
- Selenium wraps all these and makes it easier
- It also allowed implemented workarounds for cross browser support (i.e. XPATH on IE)


Types of Locators
-----------------

- By.ID
- By.NAME
- By.TAG_NAME
- By.LINK_TEXT
- By.PARTIAL_LINK_TEXT
- By.CLASS_NAME
- By.CSS_SELECTOR
- By.XPATH


Using Locators
--------------

- import By: 
	```python
	from selenium.webdriver.common.by import By
	```
- find element by locator type
	```python
	driver.find_element_by_id("my-id")
	driver.find_element_by_tag_name("div")
	```
- find element:
	```python
	driver.find_element(By.ID, "my-id")
	driver.find_element(By.NAME, "my-name")
	driver.find_element(BY.CLASS_NAME, "my-class")
	```
- locators are just string "constants"
	```python
	print(By.ID) # 'id'
	print(BY.CSS_SELECTOR) # 'css selector'
	print(BY.PARTIAL_LINK_TEXT) # 'partial link text'
	```
- python doesn't have constants -- convention is to use ALL_CAPS variable names
- You can just use strings for locator strategy
	```python
	driver.find_element("id", "my-id")
	driver.find_element("xpath", "//table[@class='results'/tbody/tr[2]/td[1]")
	```


Search Context
--------------

- Both WebDriver and WebElement implement `SearchContext`
- So you can do this:
	```python
	element = driver.find_element(By.ID, "my-id")
	nested_element = element.find_element(By.TAG_NAME, "a")
	```


Locators are tuples
-------------------

- a locator strategy, the locator 
	```python
	By.ID, "my-id"
	(By.NAME, "my-name")
	```
- you can assign it a variable to use later (or again)
	```python
	my_locator = By.CSS_SELECTOR, "#my-id > div[name=my-name]"
	type(my_locator)
	```
- driver.find_by() is a function that takes two arguments
	```python
	driver.find_element(By.CSS_SELECTOR, ".product-description")
	```
- need to unpack the tuple with * operator (not multiplication)
	```python
	driver.find_element(*my_locator)	
	```


Locator strategy preference
---------------------------

- ID is the preferred locator 
	- (id should be unique)
- NAME should also be unique 
	- (at least unique per form)
- TAG_NAME likely to return multiple elements
- CLASS_NAME can be used sometimes 
	-(but CSS_SELECTORS can incorporated easily)
- XPATH can be very precise 
	- (but also complex)
- CSS_SELECTOR almost as powerful as XPATH
	- (but cleaner)
	- (and likely to be know by front end developers)
- LINK_TEXT can change (for example "Login" can be changed to "Sign In")
	- also localization (different language versions of site "Hola" vs "Hello")
- ONLY XPATH 
	- can find by relative XPATH -- siblings, etc
	- can find by text nodes
- CSS easy for ID and CLASS NAME
	```
	#my-id
	.my-class-name
	```

Attribute or Structure base locators
------------------------------------

	- Locate by Attribute focus on attributes of the element
		- (id, class name, etc)
	- Locate by Structure foxues on structure of the document 
		- path from root
		- (parent, child relationships)
	- Finding by attributes is preferred
		- (But sometimes doesn't work)
	- Finding by structure is brittle because elements can move based on redesign that doesn't affect functionality
	- Bad XPATH (or CSS) locators are typically structure based

Selenium 4 relative locators
----------------------------

- Up and coming in Selenium 4
- Can be experimented with `pip install selenium==4.0.0.rc1`
- Find element relative to the position of another element (or locator)
	```
	above(element)
	below(element)
	near()
	to_left_of()
	to_right_of()
	```
- I don't like to use in general because they can change based on responsive layout
- Currently available in Selenium 4 beta (doesn't work with `find_element`)

`pyenv virtualenv 3.9.6 se4`
`pyenv activate se4`
`pip install selenium==4.0.0.rc2`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name
driver = webdriver.Chrome()
driver.get("https://shop.one-shore.com")
products = driver.find_element(By.CSS_SELECTOR, ".product-title")
products = driver.find_elements(By.CSS_SELECTOR, ".product-title")
products[1].text
driver.find_elements(with_tag_name("article").to_left_of(products[1]))
driver.find_elements(with_tag_name("article").to_left_of(products[1]))[0].text
driver.find_elements(with_tag_name("article").to_left_of(products[1]))[1].text
driver.find_elements(with_tag_name("article").to_right_of(products[1]))[0].text
driver.find_elements(with_tag_name("article").below(products[0])).text
driver.find_elements(with_tag_name("article").near(products[0]))[0].text
driver.find_elements(with_tag_name("article").near(products[0]))[1].text
```


Using Chrome Developer Tools
----------------------------

- Inspect
- Menu 
- CTRL + SHIFT + I


XPATH
-----

- XPATH created to search XML documents
- HTML is a subset of XML
- XPATH got a bad name because of complex, difficult to understand, and brittle locators
	- often generated by tools (like Selenium IDE)
- But sometimes XPATH is the right tool
- Especially if you need to find something by (or relative to) text on the page
- Absolute vs relative XPATH:
	```
	/html/body/table/tbody/tr[3]/td[1]
	//table//td[1]
	```
	```
	/html/body/main/section/div/div/section/section/section/div/div/article
	//article
	```
- Attribute based:
	```
	//section[@id='content']
	//section[@class='featured-products clearfix']
	```


CSS SELECTORS
-------------

- CSS can have ugly absolute paths too (or clean relative paths)
	```
	html > body > table > tbody > tr:nth-of-type(3) > td:first-of-type
	table td:first-of-type
	```
- you can refer to the element and attribute
	```
	section#content
	section.featured-products
	```
- or just the attribute 
	```
	#content
	.featured-products
	[aria-label=Price]
	```