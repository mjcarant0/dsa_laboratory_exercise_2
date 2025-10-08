"""
Main program to demonstrate function overloading for adding numbers.
"""

from add_function import add, add_array
from input_checker import get_ints

def main():
    # Demonstrate adding different counts of numbers

    nums2 = get_ints("Enter two numbers (separate with space): ", 2) # Add two numbers
    print(f"The sum is: {add(nums2[0], nums2[1])}")

    nums3 = get_ints("Enter three numbers (separate with space): ", 3) # Add three numbers
    print(f"The sum is: {add(nums3[0], nums3[1], nums3[2])}")

    nums4 = get_ints("Enter four numbers (separate with space): ", 4) # Add four numbers
    print(f"The sum is: {add_array(nums4)}")

if __name__ == "__main__":
    main()