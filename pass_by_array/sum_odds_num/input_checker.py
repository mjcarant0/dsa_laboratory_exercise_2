"""
Module to check and get integer input from the user.
"""

# Function to get a valid integer input from the user
def get_int_input(prompt):
    while True:
        value = input(prompt)

        # Check if the input is a valid integer
        if value.strip().lstrip('-').isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer.")