"""
Main program for a simple arithmetic calculator.
"""

from calculator_function import add, subtract, multiply, divide
from input_checker import get_integer, get_menu_choice

# Main function to run the calculator
def main():
    print("ARITHMETIC CALCULATOR")
    print("----------------------")
    print("[1] - Addition")
    print("[2] - Subtraction")
    print("[3] - Multiplication")
    print("[4] - Division")
    print("----------------------")
    choice = get_menu_choice() # Get a valid menu choice from user

    # Ask user for two numbers
    a = get_integer("Enter first number: ")
    b = get_integer("Enter second number: ")

    if choice == '1': # Addition
        add(a, b)

    elif choice == '2': # Subtraction
        subtract(a, b)

    elif choice == '3': # Multiplication
        multiply(a, b)

    elif choice == '4': # Division
        divide(a, b)

if __name__ == "__main__":
    main()