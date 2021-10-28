import logging
import yaml
import pytest
import sys
from socket import gethostname
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers.webdriver_factory import WebDriverFactory

logging.basicConfig()
log = logging.getLogger("framework")
log.setLevel(logging.DEBUG)
log.addHandler(logging.FileHandler("framework.log"))
log.addHandler(logging.StreamHandler(sys.stdout))

@pytest.fixture
def config():
	with open("config.yml") as config_yml:
		config = yaml.safe_load(config_yml)
		log.info(f"config: {config}")
	return config


def running_on_python_anywhere():
	if "console" in gethostname():
		return True
	return False

@pytest.fixture(autouse=True)
def chrome_options(config):
	chrome_options = webdriver.ChromeOptions()
	if running_on_python_anywhere() or config['browser']['headless'] == True:
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
	return chrome_options


@pytest.fixture
def driver(config, chrome_options):
	log.info(chrome_options)
	browser = config['browser']['name']
	log.info(f"browser: {browser}" )

	if browser == "chrome":
		driver = webdriver.Chrome(options=chrome_options)
	elif browser == "firefox":
		driver = webdriver.Firefox()
	else:
		raise Exception("unsupported browser")

	yield driver

	sleep(3)
	driver.quit()



@pytest.fixture
def browser():
	driver = WebDriverFactory("config.yml").createDriver()
	yield driver
	sleep(3)
	driver.quit()
