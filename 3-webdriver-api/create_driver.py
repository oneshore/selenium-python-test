# import webdriver
from selenium import webdriver

# creating and destroying webdriver
driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver = webdriver.Safari()
driver = webdriver.Edge()
driver = webdriver.Ie()

# exploring webdriver.Chrome()

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# chrome options
options = ChromeOptions()
options.add_argument("--headless")
options.add_extension("path-to-extension")
prefs = { "download.default_directory" : "/some/directory"}
options.add_experimental_option(prefs)

### chrome driver optional parameters
driver = ChromeDriver(
	chrome_options=options,
	executable_path="/path/to/chromedriver.exe",
	port=1234,
	service_args="args",
	service_log_path="/path/to/logs",
	desired_capabilities={"platform": "Windows", "version": "latest"}
)

### driver properties
driver.name
driver.capabilities
driver.session_id


### page properties
driver.current_url
driver.title
driver.page_source
driver.window_handles
driver.current_window_handle

#### navigation
driver.get("url")
driver.refresh()
driver.back()
driver.forward()

#### switch
driver.switch_to_window
driver.switch_to_alert
driver.switch_to.
