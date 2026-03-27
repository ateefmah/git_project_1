"""Basic calculator operations."""
import math

def add(a, b):
    """Add two numbers."""
    print(f"[DEBUG] Adding {a} + {b}")
    result = a + b
    print(f"[DEBUG] Result: {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    print(f"[DEBUG] Subtracting {a} - {b}")
    result = a - b
    print(f"[DEBUG] Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    print(f"[DEBUG] Multiplying {a} * {b}")
    result = a * b
    print(f"[DEBUG] Result: {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Divide by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def square_root(a):
    """Calculate square root of a."""
    print(f"[DEBUG] Square root of {a}")
    if a < 0:
        print(f"[DEBUG] Error: Negative number!")
        raise ValueError("Cannot calculate square root of negative number")
    result = math.sqrt(a)
    print(f"[DEBUG] Result: {result}")
    return result
