import sys
import pytest
import yaml
import logging
from time import sleep
from selenium import webdriver

logging.basicConfig()
log = logging.getLogger("framework")
log.setLevel(logging.DEBUG)
log.addHandler(logging.FileHandler("framework.log"))
log.addHandler(logging.StreamHandler(sys.stdout))

@pytest.fixture
def driver():
	driver = webdriver.Chrome()
	yield driver
	sleep(3)
	driver.quit()

def test_launch_browser(driver):
	driver.get("https://shop.one-shore.com")
	log.info(driver.title)
