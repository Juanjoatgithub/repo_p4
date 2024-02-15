import pytest

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El factorial solo puede calcularse para enteros")
    if n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def test_factorial_of_1_is_1():
    assert factorial(1) == 1

def test_factorial_raises_type_error_for_non_integer():
    with pytest.raises(TypeError):
        factorial('a')

def test_factorial_raises_value_error_for_negative_integer():
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_of_5_is_120():
    assert factorial(5) == 120
