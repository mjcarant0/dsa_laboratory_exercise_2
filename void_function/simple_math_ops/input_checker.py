"""
Module for input validation functions.
"""

# Function to get a valid integer input from the user
def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        # Check for negative integer
        if value.startswith('-'):
            value_check = value[1:]
            if value_check.isdigit():
                return int(value)
        # Check for positive integer
        elif value.isdigit():
            return int(value)
        print("Invalid input. Please enter an integer (no decimals or characters).")

# Function to get a valid menu choice from the user
def get_menu_choice():
    valid_choices = ['a', 's', 'm', 'd', 'x']
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter one of the given letters (A, S, M, D, X).")