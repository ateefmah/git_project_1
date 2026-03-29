"""This module contains functions to validate values and operations."""

def validate_number(value):
    """Validate that value can be converted to a number."""
    try:
        """Attempt to cast to number, return true if successful"""
        float(value)
        return True
    except (ValueError, TypeError):
        """Otherwise return false"""
        return False

def validate_operation(op):
    """Validate that operation is supported."""
    valid_ops = ['+', '-', '*', '/']
    """Return whether operation is part of set of supported operations"""
    return op in valid_ops

def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        """Return whether number is >= 0"""
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        """Return false if error arose casting to number"""
        return False
        
def is_positive(n):
    """Check if a number is positive."""
    return n > 0
