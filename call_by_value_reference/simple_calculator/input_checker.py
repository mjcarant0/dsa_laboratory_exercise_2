"""
Handles input validation for calculator.
"""

# Function to get a valid integer from user
def get_integer(prompt):
    # Loop until a valid integer is entered
    while True:
        value = input(prompt)
        if value.strip().lstrip('-').isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer.")

# Function to get a valid menu choice from user
def get_menu_choice():
    valid_choices = ['1', '2', '3', '4']
    
    # Loop until a valid choice is entered
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")