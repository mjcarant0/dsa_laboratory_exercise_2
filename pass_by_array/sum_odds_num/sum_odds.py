"""
Module to calculate the sum of odd numbers in a list.
"""

# Function to calculate the sum of odd numbers in a list
def sum_of_odds(numbers):
    odds = [num for num in numbers if num % 2 != 0] # To filter odd numbers
    return odds, sum(odds)