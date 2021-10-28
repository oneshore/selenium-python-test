from behave import *
from pages.home_page import HomePage
from pages.search_page import SearchPage

@given(u'I am on the shop home page')
def open_home_page(context):
	homePage = HomePage(context.driver)
	homePage.open()
	assert homePage.is_current_page()

@when(u'I search for "{searchtext}"')
def search_for_product(context, searchtext):
	homePage = HomePage(context.driver)
	assert homePage.is_current_page()
	homePage.search_for_product(searchtext)

@then(u'I should see "{number:d}" items')
def verify_search_results(context, number):
	searchPage = SearchPage(context.driver)
	assert searchPage.is_current_page()
	results = searchPage.get_search_results()
	assert len(results) == number
	context.results = results

@then(u'each item should be a "mug"')
def check_results(context):
	for item in context.results:
		print(item.text)
		assert "mug" in item.text.lower()
