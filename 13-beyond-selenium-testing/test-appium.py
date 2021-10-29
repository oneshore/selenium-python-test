# pip install Appium-Python-Client

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.touch_action import TouchAction

appium_url = "http://localhost:4723"
capabilities = {
  "device": "Pixel_5_API_30",
  "platformName": "Android",
  "platformVersion": "11.0",
  "app": "/Users/aaronevans/Downloads/2048_3.0.apk"
}
driver = webdriver.Remote(appium_url, capabilities)

start = driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='Start Game']")
start.click()

TouchAction(driver).press(x=650, y=915).move_to(x=650, y=915+100).release.perform()

driver.quit()
