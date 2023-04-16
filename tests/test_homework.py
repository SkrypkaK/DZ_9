import pytest
from src.homework import cool_piecewise_function
# из директ. и файла homework импртируем функию cool_

def test_cool_piecewise_function_for_x_less_than_minus_six():
    x = -10
    assert cool_piecewise_function(x) == 25
# присв. значение переменной х -10 делаем проверку будет ли равняться 25?

def test_cool_piecewise_function_for_x_between_minus_five_and_two():
    x = 0
    assert cool_piecewise_function(x) == 0
# проверяем математ. действие x ** 2 при условии -5 < x < 2 (х=0) - должно получиться 0.

def test_cool_piecewise_function_for_x_greater_than_or_equal_to_two():
    x = 5
    assert cool_piecewise_function(x) == -11
# проверяем математ. действие x >= 2  (где х=5)  при условии -5 * (x - 2) + 4 должно получиться -11

def test_cool_piecewise_function_for_x_between_minus_six_and_minus_five():
    x = -5.5
    assert cool_piecewise_function(x) == None

def test_cool_piecewise_function_returns_int_or_float_or_none():
    x = 1
    assert isinstance(cool_piecewise_function(x), (int, float, type(None)))


