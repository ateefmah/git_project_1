"""Basic calculator operations."""

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
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def modulo(a, b):
    """Return remainder of a divided by b."""
    print(f"[DEBUG] Modulo {a} % {b}")
    if b == 0:
        print(f"[DEBUG] Error: Modulo by zero!")
        raise ValueError("Cannot modulo by zero")
    result = a % b
    print(f"[DEBUG] Result: {result}")
    return result
