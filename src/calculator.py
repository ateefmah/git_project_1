"""Basic calculator operations."""
import math

"""Comment added."""
"""
Calculator module providing basic arithmetic operations.

Supports addition, subtraction, multiplication, division, and modulo.
Raises ValueError for invalid operations such as division or modulo by zero.
"""
# Experimental: this module may be extended with trigonometric functions

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return a / b

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)
  
def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
