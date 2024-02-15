"""
Módulo que proporciona una función para calcular el factorial de un número entero no negativo.
"""

import pytest

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parameters:
    n (int): El número entero para calcular el factorial.

    Returns:
    int: El factorial de n.

    Raises:
    TypeError: Si n no es un entero.
    ValueError: Si n es un entero negativo.
    """
    if not isinstance(n, int):
        raise TypeError("El factorial solo puede calcularse para enteros")
    if n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def test_factorial_of_1_is_1():
    """
    Prueba unitaria para verificar que el factorial de 1 es igual a 1.
    """
    assert factorial(1) == 1

def test_factorial_raises_type_error_for_non_integer():
    """
    Prueba unitaria para verificar que se levanta un TypeError 
    cuando se pasa un valor no entero a la función factorial.
    """
    with pytest.raises(TypeError):
        factorial('a')

def test_factorial_raises_value_error_for_negative_integer():
    """
    Prueba unitaria para verificar que se levanta un ValueError 
    cuando se pasa un entero negativo a la función factorial.
    """
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_of_5_is_120():
    """
    Prueba unitaria para verificar que el factorial de 5 es 120.
    """
    assert factorial(5) == 120
