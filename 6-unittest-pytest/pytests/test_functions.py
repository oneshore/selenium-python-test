import pytest

def test_addition():
	assert 1+1 == 2

def test_subtraction():
	assert 2-1 == 1

def testmultiply():
	assert 3*3 == 8

@pytest.mark.five
def test_division():
	print("testing division")
	assert 10 / 2 == 5

@pytest.mark.five
def test_another_addition():
	assert 3+2 == 5
