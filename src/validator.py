"""Provide functions to validate user inout for the calculator application"""

#temp update for checkpoint4
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

def validate_positive(n):
    """Validate that a number is positive."""
    try:
        num = float(n)
        return num > 0
    except (ValueError, TypeError):
        return False

def is_positive(n):
    """Check if a number is positive."""
    return n > 0
def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        """Return whether number is >= 0"""
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        """Return false if error arose casting to number"""
        return False
        
def validate_range(value, min_val=-1000, max_val=1000):
    """Validate that number is within acceptable range."""
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False

def is_positive(n):
    """Check if a number is positive."""
    return n > 0
