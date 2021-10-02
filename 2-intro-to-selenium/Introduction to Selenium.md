Introduction to Selenium
========================

What is Selenium?
-----------------

- Tool for automating browser actions
- Cross browser / Cross Platform
- Mimics real world user behavior
- Primarily used for writing Test Automation
- Available for many Programming Languages & Platform
- W3C Standard
- Open Source & Free
- Most popular automation tool
- Does not automate native applications*

 
History of Selenium
-------------------

- Originally written (started) in 2004 by Jason Huggins
- Jason worked at Thoughtworks on a Time & Expense tracking application
- Finding lots of bugs on different browsers
- Used Javascript to interact with web app via DOM
- This meant it could not work across sites (Cross Site Scripting protection)
- Designed with cross browser execution from the start
- Selenium RC (remote control) was developed to allow remote execution (and avoid having to embed)
- Selenium IDE created by Shinya Kasatani and donated to Selenium Project in 2006
- Selenium IDE was a Firefox plugin that allowed record and playback
- Allowed tests to be written by people with limited programming experience

Selenium Name
-------------

- Existing open source tools focused on automating a single browser (i.e. Internet Explorer via COM+)
- Commercial tools were very expensive
- Leading vendor of Commercial automation tools was "Mercury Interactive" with WinRunner (and later Quick Test Pro)
- Selenium was chosen as the name because it was thought to be a cure for "Mercury" poisoning
- Original name was "Javascript Test Runner"


History of WebDriver
--------------------

- WebDriver was developed independently of Selenium 
- Created by Simon Stewart with team Thoughtworks and Google in 2007
- Goal of isolating browser automation from testing tool
- Originally a wrapper around HttpUnit -- which communicated directly with web server (leaving browser out)
- Merged with Selenium project in 2009 
- WebDriver became underlying adapter to Selenium RC 2.0 (WebDriverBackedSelenium) in 2011
- Selenium 3.0 adopted WebDriver API over older Selenium API
```
	selenium.open(url)
	webdriver.get(url)
	selenium.click(locator)
	webdriver.find_element(locator).click()

```
- Selenium / Webdriver are now used interchangably in the project


Selenium Architecture
---------------------

- Three tools: client library for each language, driver to communicate with each browser, server for remote execution
- Client / Server Architecture
- JSON Wire Protocol (W3C WebDriver Protocol slight variation)
- Selenium Client Library (for language, e.g. Python, Java, C#) commands
- Browser Driver (e.g. ChromeDriver, EdgeDriver, FirefoxDriver, SafariDriver)
- Driver has a local web server
- Client communicates with driver using HTTP over JSON protocol (REST API)
- Driver communicates with native browser automation steps
- Commands wrap Javascript + DOM interaction in "Atoms" such as click or send_keys
- Selenium Server allows for remote execution over JSON protocol
- Selenium Grid allows for execution on an array of different platforms / browsers


Goals of Selenium Project
-------------------------

- Run across multiple browsers
- Behave like a real user
- Able to execute remotely
- Separate browser automation implementation
- Free & Open Source


How is Selenium Used
--------------------

- Allows for automating tests (obviously)
- Key role in DevOps
- Testing is a bottlneck to delivery
- Provides faster feedback
- Automation allows for continuous delivery
- Flow is more important than speed (tortoise and hare)
- improved coverage - run tests on multiple platforms
- frees up testers to do exploratory instead of regression testing
- running in parallel allows for executing more tests
- mapping automated tests to requirements, specifications (BDD) gives business more feedback for decisionmaking
- webdriver protocol used by Appium for mobile testing as well
- work to make webdriver protocol work for native apps too


Selenium Server 
--------------

- Written by Paul Hammant 

Selenium Grid
-------------

- Created in 2008 by Phillpe Hanrigou at Thoughtworks


Selenium IDE
------------

- Selenium IDE had long been without a maintainer
- Firefox upgrades broke Selenium IDE
- Developers stepped up to write Selenium IDE as a cross-browser extension
- Sponsored by Applitools
- Based on the original "Selenese" syntax: command, target, value
```
	type input value
	click button
	gettext h1
```
- command, target, value, description
- alternate targets

		
### Install Chrome (or Firefox) Extension

### Launch Selenium 

### Record Test Steps

### Run Test

### Execution Speed

### Debugging
	- step over commands
	- set breakpoints
	- pause on exceptions

### Save / Load Project
	- SIDE files

### Tests and Suites

### Log

### Reference Documentation

### Export to code

### Command line runner to run in CI/CD



### Editing Commands

###

