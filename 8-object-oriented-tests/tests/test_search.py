import pytest 
from home_page import HomePage
# use the fixtures from conftest.py to get driver

@pytest.fixture()
def homePage(driver):
	return HomePage(driver)
    
# create a pytest function 

def test_search_for_item(homePage:HomePage):
    ## use home page object 
    homePage.open()


    # assert results