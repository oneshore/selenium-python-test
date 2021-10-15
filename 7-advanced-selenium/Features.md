Features
========

Search for product
------------------

```python
find_element_by_name("s")
	input.send_keys()
	input.send_keys(Keys.Enter)
	button.click()
```

Contact us
----------

```python
find_element(By.LINK_TEXT, "Contact us").click()

locator = By.LINK_TEXT, "Contact us"
element = find_element(*locator)

```
