"""
Main program to interact with the user and compute factorial using call by reference.
"""

from factorial_function import compute_factorial
from input_checker import get_non_negative_int

def main():
    num = get_non_negative_int("Enter a number: ")
    result = [0]  # Using a list to simulate pass by reference
    compute_factorial(num, result) # Call by reference

    # Display the result
    print(f"The factorial of {num} is {result[0]}")

if __name__ == "__main__":
    main()