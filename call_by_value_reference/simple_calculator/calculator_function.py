"""
Module to perform basic arithmetic operations.
"""

# Function to add two numbers
def add(a, b):
    result = a + b
    if result.is_integer():
        print(f"The sum is: {int(result)}")
    else:
        print(f"The sum is: {result}")

# Function to subtract two numbers
def subtract(a, b):
    result = a - b
    if result.is_integer():
        print(f"The difference is: {int(result)}")
    else:
        print(f"The difference is: {result}")

# Function to multiply two numbers
def multiply(a, b):
    result = a * b
    if result.is_integer():
        print(f"The product is: {int(result)}")
    else:
        print(f"The product is: {result}")

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        print("Undefined!")
    elif a == 0 and b == 0:
        print("Undefined!")
    else:
        result = a / b
        if result.is_integer():
            print(f"The quotient is: {int(result)}")
        else:
            print(f"The quotient is: {result}")