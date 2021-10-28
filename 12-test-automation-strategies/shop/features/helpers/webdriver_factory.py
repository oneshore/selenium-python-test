import os
import logging
import yaml
from typing import Dict
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class WebDriverFactory:

	def setup_logging(self):
		logging.basicConfig()
		self.log = logging.getLogger(self.__class__.__name__)
		self.log.setLevel(logging.DEBUG)

	def __init__(self, file=None, config:Dict=None):
		self.setup_logging()
		self.config = {}
		print(self.config)

		# read config yaml file if specified and merge with config
		print(file)
		if file:
			self.log.debug(f"reading config file: {file}")
			with open(file) as config_file:
				config_yaml = yaml.safe_load(config_file)
				self.config.update(config_yaml)
				self.log.debug(f"config: {config}")

		# add config parameters if specified
		if config and len(config) != 0:
			self.config.update(config)
			self.log.debug(f"config: {config}")

		# set environment variables for path to webdriver executbales
		driver_paths = ['webdriver.chrome.driver',
			'webdriver.edge.driver', 'webdriver.gecko.driver']
		for driver_path in driver_paths:
			if driver_path in self.config:
				os.environ[driver_path] = self.config[driver_path]
				self.log.debug(f"set environment variable {driver_path} = {self.config[driver_path]}")

	def createDriver(self, browser=None, path=None, remote=False) -> WebDriver:

		# get browser from config or use default browser
		if not browser:
			if self.config["browser"]:
				browser = self.config["browser"]
				self.log.debug(f"got browser from config: {browser}")
			else:
				browser = "chrome"
				self.log.debug(f"using default browser: {browser}")

		# convert browser string to lowercase to standardize
		browser = browser.lower()
		self.log.debug(f"creating browser driver {browser}")

		# check for headless browser config
		if self.config['headless']:
			headless = True
		else:
			headless = False
		self.log.debug(f"headless: {headless}")

		# setup and create chrome webdriver instance
		if browser == "chrome":
			if path:
				os.environ['webdriver.chrome.driver'] = path

			chrome_options = self.get_chrome_options(headless)
			driver = webdriver.Chrome(options=chrome_options)

		# setup and create firefox webdriver instance
		elif browser == "firefox":
			if path:
				os.environ['webdriver.gecko.driver'] = path
			firefox_options = self.get_firefox_options(headless)
			firefox_profile = webdriver.FirefoxProfile()
			driver = webdriver.Firefox(options=firefox_options, firefox_profile=firefox_profile)

		# setup and create edge webdriver instance
		elif browser == "edge":
			if path:
				os.environ['webdriver.edge.driver'] = path
			driver = webdriver.Edge()

		return driver


	def get_chrome_options(self, headless=False):
		chrome_options = webdriver.ChromeOptions()

		# set headless chrome options
		if headless:
			self.log.debug(f"using headless chrome")
			chrome_options.add_argument("--headless")
			chrome_options.add_argument("--disable-gpu")

		self.log.debug(f"chrome options {chrome_options}")
		return chrome_options


	def get_firefox_options(self, headless:False):
		firefox_options = webdriver.FirefoxOptions()

		# set headless firefox options
		if headless:
			self.log.debug(f"using headless firefox")
			firefox_options.headless = True

		self.log.debug(f"firefox options {firefox_options}")
		return firefox_options
