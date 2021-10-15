from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from socket import gethostname
import pytest

@pytest.fixture
def driver():
	chrome_options = webdriver.ChromeOptions()

	if "console" in gethostname():
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")

	driver = webdriver.Chrome(options=chrome_options)

	yield driver

	driver.quit()

def test_submit_contact_form(driver):
	contact_url = "https://shop.one-shore.com/index.php?controller=contact"
	driver.get(contact_url)
	assert driver.title == "Contact us"

	# select dropdown
	#Full Xpath
	form_subject = driver.find_element(By.XPATH, '//*[@class="contact-form"]//select')
	select = Select(form_subject)
	select.select_by_visible_text("Webmaster")

	# enter email address
	#CSS Selector
	form_email = driver.find_element(By.CSS_SELECTOR,"form > section > div:nth-child(3) > div > input")
	form_email.send_keys("abc@xyz.com")

	# enter message
	#By Xpath
	form_msg = driver.find_element(By.XPATH,'//*[@id="content"]/section/form/section/div[5]/div/textarea')
	form_msg.send_keys("This is experiment for Automtion Training Class!")

	# press enter on message (submits)
	#By Xpath
	form_btn = driver.find_element(By.XPATH,'//*[@id="content"]/section/form/footer/input[3]')
	form_btn.send_keys(Keys.ENTER)

	# finding confirmation message
	#By CSS
	success_msg = driver.find_element(By.CSS_SELECTOR,"#content > section > form > div > ul > li")
	assert success_msg.text == "Your message has been successfully sent to our team."
	print(success_msg.text)


@pytest.mark.navigate
def test_navigate_to_contact_form(driver):

	# open home page
	driver.get("https://shop.one-shore.com")

	# click contact us on home page
	contact_form = driver.find_element(By.XPATH,'//*[@id="contact-link"]/a')
	contact_form.click()

	assert driver.title == "Contact us"

if __name__ == "__main__":
	driver = webdriver.Chrome()
	test_submit_contact_form(driver)
	driver.quit()
