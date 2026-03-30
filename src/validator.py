"""Input validation for calculator."""

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
