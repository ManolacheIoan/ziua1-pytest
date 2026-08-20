from calculator import add, subtract, divide, multiply, is_even, is_positive, power
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(7) == False

def test_is_even_zero():
    assert is_even(0) == True

def test_is_positive_true():
    assert is_positive(5) == True

def test_is_positive_false():
    assert is_positive(-3) == False

def test_is_positive_zero():
    assert is_positive(0) == False

def test_power():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1

@pytest.fixture
def sample_numbers():
    return (10, 5)

def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtract_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected