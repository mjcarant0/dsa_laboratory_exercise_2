"""
Module to compute the factorial of a number using call by reference.
"""

def compute_factorial(n, result_ref):
    factorial = 1 # Initialize factorial
    # Calculate factorial
    for i in range(1, n + 1):
        factorial *= i
    result_ref[0] = factorial