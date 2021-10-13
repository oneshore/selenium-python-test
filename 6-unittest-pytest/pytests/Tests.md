Tests 
=====

You need *something* to test

- System under test (Your application)
- Specification 
- TestCase (The test code)
- Test Runner (Pytest, Unittest)
- Framework (what you create with test test runner) 
- Automation (your selenium code)
- Libraries (Selenium)


What constitutes a test:
- A test has 1 or more steps
- A test needs to have an expected result (hypothesis, assumption)
- And test the outcome of the steps against the expected result

Tests have one of three possible outcomes:
- PASSED
- FAILED
- ERROR

An ERROR is not a FAILED test. 
It is a test that did not complete.

A test must have completed all steps to be a valid PASS or FAILURE.

A PASSING test is not a test that completed.
It also has to have "tested" something -- have an assertion that evaluates to True.

Assertions throw AssertionError if the expression evaluates to False

