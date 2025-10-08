"""
Module for basic mathematical operations.
"""

# Class containing static methods for math operations
class MathOperations:
    @staticmethod
    def add(a, b): # Addition
        print(f"The sum is {a + b}")

    @staticmethod
    def subtract(a, b): # Subtraction
        print(f"The difference is {a - b}")

    @staticmethod
    def multiply(a, b): # Multiplication
        print(f"The product is {a * b}")

    @staticmethod
    def divide(a, b): # Division
        # Avoid division by zero
        if b != 0:
            print(f"The quotient is {a // b}")
        else:
            print("Undefined!")