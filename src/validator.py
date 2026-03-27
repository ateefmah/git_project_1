"""This module contains functions to validate values and operations."""

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

def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        return False
