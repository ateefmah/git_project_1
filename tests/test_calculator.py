"""Tests for calculator operations"""
import pytest
from src.calculator import add, subtract, multiply, divide, power, modulo, square_root
from src.validator import validate_positive
from src.validator import validate_non_negative
from src.validator import validate_range

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1

def test_validate_positive():
    assert validate_positive(5) == True
    assert validate_positive(-5) == False
    assert validate_positive(0) == False
def test_square_root():
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(2) == pytest.approx(1.414, rel=0.01)

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-1)

def test_validate_non_negative():
    assert validate_non_negative(5) == True
    assert validate_non_negative(0) == True
    assert validate_non_negative(-5) == False
  
def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(7, 2) == 1

def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(5, 0)

def test_range_validation():
    assert validate_range(100) == True
    assert validate_range(2000) == False
    assert validate_range(-2000) == False
