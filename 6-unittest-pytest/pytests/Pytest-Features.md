Pytest Features
---------------


function test

class tests

assert

running

finding tests and naming conventions - auto discovery

fixtures

marking

running unittest tests

parameterize

data driven

reporting

code coverage

hooks

plugins

pytest-selenium

xdist - parallel execution



### Assertions

The `assert` keyword is a native python construct

`assert (expression)`
`assert 1+1 == 2`

`assert` raises `AssertionError` if expression does not evaluate to `True`


### Hooks

reference: https://docs.pytest.org/en/6.2.x/reference.html#hooks

#### boostrapping hooks

only for internal and setuptools 

- pytest_load_initial_conftests()
- pytest_cmdline_preparse()
- pytest_cmdline_parse()
- pytest_cmdline_main()

#### initialization hooks

 called for plugins and conftest.py files.

 - pytest_addoption()
 - pytest_addhooks()
 - pytest_configure()
 - ...

#### collection hooks

#### testrunning hooks

#### reporting hooks

#### debugging / interaction hooks

`conftest.py` can define hooks (and fixtures)

parallel testing
----------------

`pip install pytest-xdist` 