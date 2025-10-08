"""
Main program to demonstrate function overloading for substring extraction.
"""

from input_checker import get_valid_index
from substring_function import substring

def main():
    # Original string
    s = "the quick brown fox jumps over the dog..."
    print(f"Original string value:\n{s}")
    print(f"String length: {len(s)}\n")

    # Get valid start and end indices from the user
    start = get_valid_index("Enter start index: ", 0, len(s)-1)
    end = get_valid_index("Enter end index: ", start, len(s)-1)
    print()

    # Demonstrate the overloaded substring function
    substring(s)
    print()
    substring(s, start)
    print()
    substring(s, start, end)

if __name__ == "__main__":
    main()