from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from helpers.webdriver_factory import WebDriver, WebDriverFactory
from helpers.webdriver_factory import *

import os

os.popen("lighthouse \
			--view \
			--quiet \
			--no-update-notifier \
			--no-enable-error-reporting \
			--output=html \
			--output-path=perf.results.html \
			https://shop.one-shore.com/index.php")



