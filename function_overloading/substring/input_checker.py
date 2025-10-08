"""
Module for input validation functions.
"""

def get_valid_index(prompt, min_value, max_value):
    # Ask the user until a valid index is entered
    while True:
        value = input(prompt)
        if value.isdigit():
            idx = int(value)
            
            # Check if the index is within the valid range
            if min_value <= idx <= max_value: 
                return idx
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a valid integer.")