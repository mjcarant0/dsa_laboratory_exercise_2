"""
Main program to get 10 integers from the user,
display them, and calculate the sum of odd numbers.
"""

from input_checker import get_int_input
from sum_odds import sum_of_odds

# Main function
def main():
    numbers = [] # List to store user inputs
    
    # Get 10 integers from the user
    for i in range(1, 11):
        num = get_int_input(f"Enter number {i}: ")
        numbers.append(num)
    
    print(f"\nYour numbers: {' '.join(str(n) for n in numbers)}") # Display the numbers entered

    odds, total = sum_of_odds(numbers) # Calculate odd numbers and their sum
    
    # Display odd numbers and their sum
    print(f"Odd numbers: {' '.join(str(n) for n in odds) if odds else 'None'}")
    print(f"The sum of all odd numbers is {total}")

if __name__ == "__main__":
    main()