import pytest
from selenium import webdriver

def launch_browser(browsername):
    if browsername.upper() == "CHROME":
        return webdriver.Chrome()
    if browsername.upper() == "FIREFOX":
        return webdriver.Firefox()
    if browsername.upper() == "EDGE":
        return webdriver.Edge()
    if browsername.upper() == "SAFARI":
        return webdriver.Safari()

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browsername = request.param
    print(f"browsername: {browsername}")
    browser = launch_browser(browsername)
    yield browser
    browser.quit()
    
def test_browser(browser):
    print(f"browser: {browser}")
    browser.get("https://shop.one-shore.com")