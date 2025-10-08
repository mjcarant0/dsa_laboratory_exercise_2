"""
Module for input validation functions.
"""

# Function to get a valid positive float input from the user
def get_positive_float_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            num = float(value)
            if num > 0:
                return num
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number (no letters or special characters).")

# Function to get a valid menu choice from the user
def get_menu_choice():
    valid_choices = ['1', '2', '3', '4', '5']
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")