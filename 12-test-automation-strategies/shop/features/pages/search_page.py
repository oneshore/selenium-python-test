from .selenium_page import SeleniumPage
from .webdriver_helpers import *
from typing import List

class SearchPage(SeleniumPage):

	URL = "https://shop.one-shore.com/index.php?controller=search"

	search_results_header_locator = By.CSS_SELECTOR, "#js-product-list-header"

	def __init__(self, driver:WebDriver):
		super().__init__(driver, self.URL)

	def get_header(self):
		self.when_visible(SearchPage.search_results_header_locator)

	def get_search_results(self) -> List[WebElement]:
		search_results = self.driver.find_elements(By.CSS_SELECTOR, "article")
		return search_results
		#comment
