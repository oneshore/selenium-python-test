Test Automation Strategies
==========================

- Different ways you can automate
- Determines framework you will choose
- Developer focused
- Business Requirements focused
- Collaboration focused
- Maximize technology benefits
- Minimize technology needed
- Suited to the way your team works
- Suited to people's skillset

Test Driven Development (TDD)
-----------------------------

# TDD

- Term coined by Kent Beck
- part of Extreme Programming
- Write tests first
- Or at least the same time as application code
- Developer focused

## Red Green Refactor

- Write a failing test
- Write just enough code to make it pass
- Refactor code to improve structure, performance
- If test fails, too much code changed

- KISS: Keep it simple
- YAGNI: You aren't going to need it

## Benefits of TDD

- Allows for rapid iteration
- High confidence in code
	- But not suited to exploratory testing
- Writing tests with code improves code quality
	- Fewer bugs found, but more bugs prevented
- Tests act act scaffold and guard rails for code
- Makes refactoring easier
- The tests get written!

## Drawbacks of TDD

- Risk of short sightedness, technical debt
- Requires architectural & business oversight
- to avoid "painting yourself in a corner"
- or over-focusing on the details
- Can be difficult to implement Selenium tests if UI not yet defined


Behavior Drive Development (BDD)
================================

- Describe a user behavior
- Write a test that executes it
- Higher level tests
- Suitable for functional, end-to-end tests
- Business goal oriented
- Uses business domain language (Orders, Payments, etc)
- Specifications in plain English (or your language)
- Map specs to automated test code

## History

- BDD coined by Dan North
- JBehave implemetated by Dan North with Liz Keogh, others
- Extension of TDD principles


## Cucumber & Gherkin

- One (common, standardized) way to do BDD
- ubiquitous language
- Feature Files
- Step Definitions
- Hooks
- Context
- Automation Code

- Cucumber written by Aslak Hellosy
- Originally in Ruby
- Ported to Java / JS / other languages
- C# has specflow
- Python has Behave and Lettuce
- Cucumber Python project is outdated

## Stories / Features / Scenarios

### Feature File
### Specification

Title

### Narrative
### Purpose

```gherkin
As a <role>
I want to <achieve some goal>
So that <benefit or value>
```

### Scenario
### Acceptance Criteria
```gherkin
Given ... <some precondition>
When ... <some action is performed>
Then ... <some result is observed>
```
## Gherkin Example

-

## Benefits of BDD

- Think as the user when testing
- Executable specifications
- Communication between silos -- Business/Development/Testing
- Generates easy to documentation
- Common framework for thinking about (and discussing) features & requirements

## Drawbacks of BDD

- Verbose
- Tests written in clear english
	- Must be precise in language
- Must map specifications to code
- Added layer of complexity
- Little benefit of only used by tester

## Behave

- Python implementation of Cucumber
- Fully supports Gherkin

`pip install behave`

- Need behave-parallel for concurrent test
`pip install behave-parallel`
https://github.com/hugeinc/behave-parallel

### Features
- create a directory called `features`
- add a feature file called `name.feature`
- Feature files use gherkin syntax

### Step definitions
- create a directory under `features` called 	`steps`
- add a python file corresponding the feature `name.py`
- import behave `from behave import *`
- create functions for steps
- add `context` as parameter for function
- add decorators for `@given` `@when` and `@then`

```python
from behave import *

@given('some precondition')
def some_precondition(context):
	# implementation
	amount =
@when('I do something')
def i_do_something(context):
	# implementation
	context.value

@then('some result')
def some_result(context):
	assert result == True
```

### Parameters in steps

- add data to a feature file step

```
@given('I have "$100" in my account')

### Tables

### Scenario Outlines

### Hooks

- Before / After
	- all
	- tags
	- feature
	- scenario
	- step

### Context

- Keeps state *within a scenario*
- Pass data between steps


## Vs Lettuce

- uses only one `@step` decorator
- instead of `@given` / `@when` / `@then`
- `world` global context
- Hooks are decorators instead of functions
- Originally had stability issues
- And did not support tags (it does now)
- Not as actively maintained as Behave

## Vs Pytest-BDD

- Relies on Splinter (not Selenium)
- Splinter sits on top of Selenium
- But also other methods of automation
- Newer project, but gaining momementum


Keyword Driven Tests
--------------------

## Robot Framework
