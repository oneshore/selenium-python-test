import pytest
from home_page import HomePage
from search_page import SearchPage
# use the fixtures from conftest.py to get driver

@pytest.fixture()
def homePage(driver):
	return HomePage(driver)

# create a pytest function

def test_search_for_item(homePage:HomePage):
	## use home page object
	homePage.open()

	# get mugs from search results
	searchPage = homePage.search_for_product("mug")
	search_results = searchPage.get_search_results()

	# check content of search results
	print(search_results.count)
	for item in search_results:
		print(item.text)
		assert "mug" in item.text.lower()

	# assert results
	assert len(search_results) == 5
