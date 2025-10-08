"""
Main program for the Area Calculator program.
Handles user interaction and calls area calculation functions.
"""

from area_functions import AreaCalculator
from input_checker import get_positive_float_input, get_menu_choice

def main():
    # Main program loop
    while True:
        print("----------------------")
        print("MENU")
        print("----------------------")
        print("[1] - Area of square")
        print("[2] - Area of rectangle")
        print("[3] - Area of triangle")
        print("[4] - Area of circle")
        print("[5] - exit")
        print("----------------------")
        choice = get_menu_choice()

        if choice == '1': # Area of square
            print("\nAREA OF SQUARE")
            print("----------------------")
            side = get_positive_float_input("Enter the side of the square: ")
            area = AreaCalculator.area_square(side)
            print(f"\nThe area is {area} sq. units\n")

        elif choice == '2': # Area of rectangle
            print("\nAREA OF RECTANGLE")
            print("----------------------")
            length = get_positive_float_input("Enter the length of the rectangle: ")
            width = get_positive_float_input("Enter the width of the rectangle: ")
            area = AreaCalculator.area_rectangle(length, width)
            print(f"\nThe area is {area} sq. units\n")

        elif choice == '3': # Area of triangle
            print("\nAREA OF TRIANGLE")
            print("----------------------")
            base = get_positive_float_input("Enter the base of the triangle: ")
            height = get_positive_float_input("Enter the height of the triangle: ")
            area = AreaCalculator.area_triangle(base, height)
            print(f"\nThe area is {area} sq. units\n")

        elif choice == '4': # Area of circle
            print("\nAREA OF CIRCLE")
            print("----------------------")
            radius = get_positive_float_input("Enter the radius: ")
            area = AreaCalculator.area_circle(radius)
            print(f"\nThe area is {area} sq. units\n")

        elif choice == '5': # Exit
            print("Thank you!")
            input("Press any key to exit . . .")
            break

# Run the main program
if __name__ == "__main__":
    main()