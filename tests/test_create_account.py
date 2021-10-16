import os
from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def driver():
	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	driver.maximize_window()
	yield driver
	sleep(3)
	driver.quit()
