from selenium import webdriver
from selenium.webdriver.common.by import By
from socket import gethostname
# open the demo shop home page
options = webdriver.ChromeOptions()

if "console" in gethostname():
	options.add_argument("--headless")
	options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://shop.one-shore.com/")

# directly interact
driver.find_element(By.LINK_TEXT, "Contact us")

# create a locator first
contact_locator = By.LINK_TEXT, "Contact us"
contact_link = driver.find_element(*contact_locator)


# click the contact us link
contact_link.click()


# on contact form page

# select webmaster from subject
subject_locator_css = By.CSS_SELECTOR, ".contact-form > form select[name=id_contact]"
subject_locator_xpath = (By.XPATH, "//section[@class='contact-form']/form//select[@name='id_contact']")
subject_locator = By.NAME, "id_contact"
subject_dropdown = driver.find_element(*subject_locator_css)
subject_options_locator = (By.TAG_NAME, "option")
subject_options = subject_dropdown.find_elements(*subject_options_locator)
for option in subject_options:
    print(option.text, option.get_attribute("value"))
    if option.text == "Webmaster":
        if not option.is_selected():
            option.click()

# enter email address
email_locator = By.XPATH, "//section[@class='contact-form']//input[@type='email']"
email_field = driver.find_element(*email_locator)
email_field.send_keys("email@example.com")

# enter message
message_locator = By.CSS_SELECTOR, ".contact-form textarea"
message_textarea = driver.find_element(*message_locator)
message_textarea.send_keys("I love your website, but it's difficult to automate")

send_button = By.XPATH, "//input[@type='submit'][@value='Send']"
driver.find_element(*send_button).click()

alert_message_locator = By.CSS_SELECTOR, ".contact-form .alert"
message = driver.find_element(*alert_message_locator)

print(message.text)


driver.quit()
