from time import sleep
from helpers.webdriver_factory import WebDriverFactory
import yaml
import os

def before_scenario(context, scenario):

	with open("config.yml") as config_yml:
		config = yaml.safe_load(config_yml)
		print()
		print(f"config: {config}")

	context.driver = WebDriverFactory("config.yml").createDriver()

def after_scenario(context, scenario):
	sleep(3)
	context.driver.quit()
