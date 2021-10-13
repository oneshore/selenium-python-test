Introduction to Pytest
======================

Why use a testing framework
---------------------------

Pytest
------

- Most popular
- Can run unittest tests
- Finds tests automatically
- Can be used for all types of tests:
	- unit tests
	- API tests
	- Selenium based tests
	- Other tests

Install pytest
--------------

`pip install pytest`

`conda install pytest`

Execute pytest
--------------

```python
	pytest # searches from current folder recursively
	pytest <options> #options
	pytest /path/to/folder # searches from speficied folder
	pytest file.py # searches specified file
	pytest -v # shows all tests, not just failing (verbose)
	python -m pytest <options> # run as module with specific python
```


How Pytest finds tests
----------------------

- looks for files that start with test_*.py or end with *_test.py
- will find in current folder by default
- or specified folder
- will recursively look through subdirectories
- functions must start with test*
- classes must start with Test* (capitalized)
- __init__() method should not exist

Showing output
-------------
```python
pytest -s # capture=no -- print output
pytest -v # verbose -- list all tests, not just failing
pytest -r A # show all
```

Select specific tests with marks (tags)
---------------------------------------

```
import pytest

@pytest.mark.mytag
def my_test():
	assert True
```

Call pytest with -m

```python
pytest -m mytag --disable-warnings
```

Call multiple tags

```python
pytest -m "tag1 and tag2"
pytest -m "tag1 or tag2"
pytest -m "not tag2"
```

tag all tests in file

```pytest
pytestmark = pytest.mark.mytag
pytestmark = [pytest.mark.mytag, pytest.mark.anothertag]
```


pytest reports
--------------

pytest-html
add screenshots

allure reports

install allure on machine:
	windows:
	`scoop install allure`

	mac:
	`brew install allure`

	linux (debian/ubuntu):
	```
	sudo apt-add-repository pp:qameta/allure
	sudo apt-get update
	sudo apt-get install allure
	```
