"""Provides functions to validate user inout for the calculator application"""

def validate_number(value):
    """Validate that value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def validate_operation(op):
    """Validate that operation is supported."""
    valid_ops = ['+', '-', '*', '/']
    return op in valid_ops

def validate_positive(n):
    """Validate that a number is positive."""
    try:
        num = float(n)
        return num > 0
    except (ValueError, TypeError):
        return False
