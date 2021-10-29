# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["device"] = "Pixel_5_API_30"
caps["platformName"] = "Android"
caps["platformVersion"] = "11.0"
caps["app"] = "/Users/aaronevans/Downloads/2048_3.0.apk"
caps["ensureWebviewsHavePages"] = True
caps["nativeWebScreenshot"] = True
caps["chromeOptions"] = {"w3c":False}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.Button[1]")
el1.click()
TouchAction(driver)   .press(x=211, y=1149)   .move_to(x=435, y=1153)   .release()   .perform()

TouchAction(driver)   .press(x=911, y=1606)   .move_to(x=924, y=1368)   .release()   .perform()


driver.quit()
