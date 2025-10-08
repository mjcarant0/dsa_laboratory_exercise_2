<div align="center">

# Area Calculator

</div>

## How the Code Works

### A. **area_functions.py**

##### 1. **Defining the AreaCalculator Class**
```python
class AreaCalculator:
    @staticmethod
    def area_square(side: float) -> float:
        return side * side

    @staticmethod
    def area_rectangle(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def area_triangle(base: float, height: float) -> float:
        return 0.5 * base * height

    @staticmethod
    def area_circle(radius: float) -> float:
        return 3.141592653589793 * radius * radius
```
- **Purpose:** Provides static methods to calculate the area of a square, rectangle, triangle, and circle.
- **How:**  
  - Each method takes the required dimensions as arguments and returns the computed area.
  - Uses the standard formula for each shape.

---

### B. **input_checker.py**

##### 1. **Input Validation Functions**
```python
def get_positive_float_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            num = float(value)
            if num > 0:
                return num
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number (no letters or special characters).")

def get_menu_choice():
    valid_choices = ['1', '2', '3', '4', '5']
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
```
- **Purpose:** Ensures the user enters valid positive numbers for dimensions and a valid menu choice.
- **How:**  
  - `get_positive_float_input` keeps prompting until a positive float is entered.
  - `get_menu_choice` keeps prompting until a valid menu option is selected.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
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
```
- **Purpose:** Provides a menu-driven interface for calculating the area of different shapes.
- **How:**  
  - Displays a menu and prompts the user for a choice.
  - For each shape, prompts for the required dimensions and computes the area using the appropriate method.
  - Handles input validation and allows the user to exit the program.

---