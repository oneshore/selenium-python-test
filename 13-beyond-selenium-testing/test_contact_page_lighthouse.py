import os
import pytest
from helpers.lighthouse import lighthouse
from helpers.webdriver_helpers import *
from shop.home_page import HomePage

@pytest.mark.lighthouse
def test_contact_page(browser):
	HomePage(browser).open().click_contact_link()
	lighthouse(browser.current_url, "contact-page.lighthouse.html")


