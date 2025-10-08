"""
Main program for simple math operations using functions from other modules.
"""

from operations import MathOperations
from input_checker import get_int_input, get_menu_choice

def main():
    # Main program loop
    while True:
        # Display menu
        print("----------------------")
        print("MENU")
        print("----------------------")
        print("[A] - addition")
        print("[S] - subtraction")
        print("[M] - multiplication")
        print("[D] - division")
        print("[X] - exit")
        print("----------------------")
        choice = get_menu_choice()

        if choice == 'a': # Addition
            print("\nADDITION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.add(a, b)

        elif choice == 's': # Subtraction
            print("\nSUBTRACTION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.subtract(a, b)

        elif choice == 'm': # Multiplication
            print("\nMULTIPLICATION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.multiply(a, b)

        elif choice == 'd': # Division
            print("\nDIVISION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.divide(a, b)

        elif choice == 'x': # Exit
            print("\nThank you!")
            input("Press any key to exit . . .")
            break

# Run the main function
if __name__ == "__main__":
    main()