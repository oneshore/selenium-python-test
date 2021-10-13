Unit Test
---------

- vs integration Test
- vs other frameworks (pytest, nose, doctest)

unittest is included with python

```python
import unittest
```

Test Case
---------

- test case (create a class that extends unittest.TestCase)
- methods start with test_*

Running tests
-------------

```python
if __name__ == "__main__":
	unittest.main()
```

`python mytest.py`

Discover tests
--------------

`python -m unittest -v` # -v for verbose # discover is default
`python -m unittest discover -s unittests/` # -s for start directory
`python -m unittest discover -p *tests.py` # -p for custom search pattern

Test Suites
-----------

- Suites allow you to run custom test groupings

`python unittests/testsuite.py`

Setup and Teardown
------------------




