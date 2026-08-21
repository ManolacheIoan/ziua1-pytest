def add(a, b):
    # varianta 1
    result = a + b
    return result

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def power(base, exp):
    return base ** exp

def modulo(a, b):
    return a % b