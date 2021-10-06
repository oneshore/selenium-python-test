### import webdriver module

from selenium import webdriver
type(webdriver) #=> module


### options

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

options.add_extension("path/to/extension")

prefs = { "download.default_directory" : "/some/directory"}
options.add_experimental_option(prefs)


### create webdriver client instance

driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Safari()
driver = webdriver.Edge()
driver = webdriver.Remote()


### driver properties

driver.name # => ch
driver.capabilities
driver.session_id


### Window size and position

driver.get_window_size()
driver.get_window_position()
driver.get_window_rect() # size and position
driver.minimize_window()
driver.maximize_window()

### page info

driver.current_url
driver.title
driver.page_source


### navigating

driver.get("https:///shop.one-shore.com")
driver.back()
driver.forward()
driver.refresh()

### finding elements

from selenium.webdriver.common.by import By

driver.find_element(By.ID, "id")
driver.find_elements(By.TAG_NAME, "button")

driver.find_element_by_id("id")
driver.find_element_by_name("name")
driver.find_element_by_tag_name("tag")
driver.find_element_by_link_text("link text")
driver.find_element_by_partial_link_text("text")
driver.find_elements_by_class_name("classname")
driver.find_element_by_xpath("//div[@class='classname']/button")
driver.find_element_by_css_selector(".classname > button")


### dealing with multiple windows

driver.window_handles
driver.current_window_handle

### switching between windows, frames, popups

driver.switch_to_window("window handle")
driver.switch_to_frame("frame id")
driver.switch_to_alert()
driver.switch_to_default_content()

### dealing with cookies

driver.get_cookies()
driver.get_cookie("cookiename")
driver.add_cookie({"name":"cookiename", "value":"cookievalue"})
driver.delete_cookie("cookiename")
driver.delete_all_cookies()

### execute javascript on the page

driver.execute_script("script")
driver.execute_async_script("script")
driver.create_web_element("element id")


### take screenshots

driver.get_screenshot_as_file("filename")
driver.get_screenshot_as_base64()
driver.get_screenshot_as_png()

### remote file uploads

driver.file_detector





### interacting with elements

from selenium.webdriver.remote.webelement import WebElement

element:WebElement = driver.find_element_by_id("id")

### inspecting elements

element.id
element.text
element.tag_name


### element text

element.text

# acting on web elements
element.click()
element.send_keys("text")
element.clear()
element.submit()

### element size and position

element.size
element.location
element.rect

### element status

element.is_displayed
element.is_enabled
element.is_selected

### take a screenshot of element

element.screenshot("filename")
element.screenshot_as_png
element.screenshot_as_base64

### finding elements from parent elements

element.find_element_by_class_name("classname")
element.find_elements_by_tag_name("tag")

### Getting element attributes

element.get_attribute("href")
element.get_attribute("class")
element.get_attribute("id")
element.get_attribute("name")
element.get_attribute("value")

element.get_attribute("tagName")
element.get_attribute("outerHTML")
element.get_attribute("innerHTML")
element.get_attribute("innerText")

element.get_property() # returns current, not just source
