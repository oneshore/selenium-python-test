WebDriver Architecture and API
==============================

WebDriver Architecture
----------------------

- Client => Server
- HTTP REST API
- Browser Drivers: ChromeDriver, FirefoxDriver, SafariDriver, EdgeDriver
- WebDriver -> RemoteWebDriver -> ChromeDriver
- Selenium Server
- Selenium Grid: Hub & Nodes
- Selenium API: Web Server, REST API Endpoints, HTTP, JSON payload


Python Client Bindings
----------------------

- Different Language Bindings: Python, Java, C#, Ruby, etc
- All implement the Webdriver protocol
- install selenium module

	pip install selenium
	conda install selenium

- import selenium module into python code

	from selenium import webdriver

- example

Webdriver Wire Protocol
------------------

- Capabilities
- WebElement
- Selenium 3 - JSON Wire Protocol https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol
- Selenium 4 - W3C Webdriver Protocol  https://w3c.github.io/webdriver/webdriver-spec.html



WebDriver API
-------------

- Check Server status: GET /status
- Create a new Session: POST /session
- Get list of Sessions: GET /sessions
- Destroy an existing Session DELETE /session/:id
