import os
import yaml
from typing import Dict
from selenium import webdriver

class WebDriverFactory:

	def __init__(self, config:Dict=None, file=None):
		self.config = {}

		# add config parameters if specified
		if config:
			self.config.update(config)

		# read config yaml file if specified and merge with config
		if file:
			with open(file) as config_file:
				config_yaml = yaml.safe_load(config_file)
				self.config.update(config_yaml)

		# set environment variables for path to webdriver executbales
		driver_paths = ['webdriver.chrome.driver',
			'webdriver.edge.driver', 'webdriver.gecko.driver']
		for driver_path in driver_paths:
			if self.config[driver_path]:
				os.environ[driver_path] = self.config[driver_path]


	def createDriver(self, browser="chrome", path=None, remote=False):
		browser = browser.lower()

		if browser == "chrome":
			if path:
				os.environ['webdriver.chrome.driver'] = path
			chrome_options = self.get_chrome_options()
			driver = webdriver.Chrome(options=chrome_options)

		elif browser == "firefox":
			if path:
				os.environ['webdriver.gecko.driver'] = path
			firefox_options = self.get_firefox_options()
			firefox_profile = webdriver.FirefoxProfile()
			driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)

		elif browser == "edge":
			if path:
				os.environ['webdriver.edge.driver'] = path
			driver = webdriver.Edge()

		return driver


	def get_chrome_options(self, headless=False):
		chrome_options = webdriver.ChromeOptions()
		if headless:
			chrome_options.add_argument("--headless")
			chrome_options.add_argument("--disable-gpu")
		return chrome_options


	def get_firefox_options(self, headless:False):
		firefox_options = webdriver.FirefoxOptions()
		if headless:
			firefox_options.headless = True
		return firefox_options
