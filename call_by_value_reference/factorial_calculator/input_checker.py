"""
Module to handle user input and validate it.
"""

# Function to get a valid non-negative integer from the user
def get_non_negative_int(prompt):
    while True:
        value = input(prompt)

        # Check if the input is a non-negative integer
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a non-negative integer.")