"""
Module providing functions to add numbers with different signatures.
"""

# Function to add two, three, or four numbers
def add(a, b, c=None, d=None):
    if c is None and d is None:
        # Two arguments
        return a + b
    elif d is None:
        # Three arguments
        return a + b + c
    else:
        # Four arguments
        return sum([a, b, c, d])

# Function to add an array of numbers
def add_array(arr):
    return sum(arr)