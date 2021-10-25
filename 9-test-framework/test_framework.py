import pytest
import yaml
from time import sleep
from selenium import webdriver


def test_launch_browser():
	driver = webdriver.Chrome()
	driver.get("https://shop.one-shore.com")
	sleep(3)
	driver.quit()
