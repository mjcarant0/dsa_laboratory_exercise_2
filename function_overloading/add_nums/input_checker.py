"""
Module for input validation to get a specific count of integers from user input.
"""

def get_ints(prompt, count):
    # Ask user until they enter the correct number of integers
    while True:
        try:
            values = input(prompt).split() # Split input by spaces
            if len(values) != count:
                print(f"Please enter exactly {count} numbers.")
                continue
            nums = [int(v) for v in values] # Convert to integers
            return nums
        except ValueError:
            print("Invalid input. Please enter integers only.")