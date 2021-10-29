import pytest
import logging
from sys import stdout
from selenium import webdriver
from shop.home_page import HomePage
from shop.login_page import LoginPage
from shop.search_page import SearchPage


from axe_selenium_python_dev import Axe

log = logging.getLogger("A11Y")
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler("a11y.log"))
log.addHandler(logging.StreamHandler(stdout))
logging.basicConfig()

@pytest.mark.accessibility
@pytest.mark.home
def test_accessibility():
	browser = webdriver.Chrome()
	browser.get("https://shop.one-shore.com")
	axe = Axe(browser)
	axe.inject()
	results = axe.run()
	# print("_____RESULTS_____")
	# print(results)
	axe.write_results(results, 'a11y.json')
	violations = results['violations']
	# print("____VIOLATIONS____")
	# print(violations)
	report = axe.report(violations)
	print("----REPORT----")
	print(report)
	browser.quit()

@pytest.fixture
def axe(request, browser):
	testname = request.node.name
	results_file = testname + ".a11y.json"
	axe = Axe(browser)
	yield axe
	axe.run()
	results = axe.run()
	axe.write_results(results, results_file)
	violations = results['violations']
	report = axe.report(violations)
	print("ACCESSIBILITY REPORT")
	print(report)

@pytest.mark.accessibility
@pytest.mark.login
def test_login_page(browser, axe):
	loginPage = LoginPage(browser).open()
	axe.inject()

@pytest.mark.accessibility
@pytest.mark.search
def test_search_results(browser, axe):
	homePage:HomePage = HomePage(browser).open()
	searchPage:SearchPage = homePage.search_for_product("pillow")
	axe.inject()
