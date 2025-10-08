<div align="center">

# Simple Math Operations

</div>

## How the Code Works

### A. **operations.py**

##### 1. **Defining the MathOperations Class**
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        print(f"The sum is {a + b}")

    @staticmethod
    def subtract(a, b):
        print(f"The difference is {a - b}")

    @staticmethod
    def multiply(a, b):
        print(f"The product is {a * b}")

    @staticmethod
    def divide(a, b):
        if b != 0:
            print(f"The quotient is {a // b}")
        else:
            print("Undefined!")
```
- **Purpose:** Provides static methods for addition, subtraction, multiplication, and division, printing the result directly.
- **How:**  
  - Each method takes two integer arguments and prints the result.
  - The `divide` method checks for division by zero and prints "Undefined!" if division is not possible.

---

### B. **input_checker.py**

##### 1. **Input Validation Functions**
```python
def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.startswith('-'):
            value_check = value[1:]
            if value_check.isdigit():
                return int(value)
        elif value.isdigit():
            return int(value)
        print("Invalid input. Please enter an integer (no decimals or characters).")

def get_menu_choice():
    valid_choices = ['a', 's', 'm', 'd', 'x']
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter one of the given letters (A, S, M, D, X).")
```
- **Purpose:** Ensures the user enters valid integers for operands and a valid menu choice.
- **How:**  
  - `get_int_input` keeps prompting until a valid integer (positive or negative) is entered.
  - `get_menu_choice` keeps prompting until the user selects a valid operation.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
from operations import MathOperations
from input_checker import get_int_input, get_menu_choice

def main():
    while True:
        print("----------------------")
        print("MENU")
        print("----------------------")
        print("[A] - addition")
        print("[S] - subtraction")
        print("[M] - multiplication")
        print("[D] - division")
        print("[X] - exit")
        print("----------------------")
        choice = get_menu_choice()

        if choice == 'a':
            print("\nADDITION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.add(a, b)

        elif choice == 's':
            print("\nSUBTRACTION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.subtract(a, b)

        elif choice == 'm':
            print("\nMULTIPLICATION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.multiply(a, b)

        elif choice == 'd':
            print("\nDIVISION")
            a = get_int_input("Enter first number: ")
            b = get_int_input("Enter second number: ")
            MathOperations.divide(a, b)

        elif choice == 'x':
            print("\nThank you!")
            input("Press any key to exit . . .")
            break

if __name__ == "__main__":
    main()
```
- **Purpose:** Provides a menu-driven interface for performing basic arithmetic operations.
- **How:**  
  - Displays a menu and prompts the user for a choice.
  - For each operation, prompts for two integers and calls the corresponding method.
  - Handles input validation and allows the user to exit the program.

---