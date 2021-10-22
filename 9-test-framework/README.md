Creating a Test Framework
=========================

Elements of a test framework
----------------------------

- run tests
- select subset of tests to run
- organize tests
- make tests easier to maintain (DRY)
- handle starting and stopping browsers
- configuration
- logging
- reporting
- screenshots (on failure)
- load test data
- run on multiple environments
- handle test retries


Separating tests from automation code
-------------------------------------

- page object pattern
- site object to manage pages
- separate functional steps from automation steps
- ability to replace one implementation with another
  - selenium / another automation framework
  - API call for automation
  - different steps to accomplish goal


Logging
-------

- python logging
- file and console appenders
- log levels
- per class / file logs
- filtering logs
- log rollover
- let framework handle logging
- keep majority of log messages out of tests


Configuration
-------------

- what to specify in configuration
  - browser
  - executable path (e.g. chromedriver path)
  - browser options (e.g. headless)
  - test environment
  - location of test data
  - database & other external resources
- reading a config file
- yaml
- reasonable defaults


Reporting
---------

- why reports
- reporting options
- pytest html reports
- test results in jenkins: junitxml report
- test coverage reporting


Base Test
---------

- handles fixtures for setup / teardown
- helper methods
- default wait
- loading test data
- extending tests


Driver Factory
--------------

- create webdriver instances
- browser options & profiles
- set driver executable path
- specify remote or local webdriver
- logging
