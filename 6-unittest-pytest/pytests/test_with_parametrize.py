import pytest

@pytest.mark.parametrize("num1, num2 ,expected",
                  [(2, 5, 7),
                   (3, 7, 10)])
def test_addition(num1, num2, expected):
    assert num1 + num2 == expected

division_data = [
    (4, 2, 2),
    (9, 3, 3),
    (10, 2, 5),
    (2, 2, 1)
]

@pytest.mark.parametrize("numerator, denominator, expected", division_data)
def test_division(numerator, denominator, expected):
    assert numerator/denominator == expected


