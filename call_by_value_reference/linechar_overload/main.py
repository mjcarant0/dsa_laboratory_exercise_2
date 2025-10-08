"""
Main program to demonstrate function overloading based on parameter types.
"""

from linechar_function import linechar

# Main function to call linechar with different parameters
def main():
    linechar()
    linechar('@')
    linechar(10)
    linechar('#', 15)
    input("Press any key to continue . . .") # Pause the program before exiting

if __name__ == "__main__":
    main()