<div align="center">

# Simple Calculator

</div>

## How the Code Works

### A. **calculator_function.py**

##### 1. **Defining Arithmetic Operation Functions**
```python
def add(a, b):
    result = a + b
    if result.is_integer():
        print(f"The sum is: {int(result)}")
    else:
        print(f"The sum is: {result}")

def subtract(a, b):
    result = a - b
    if result.is_integer():
        print(f"The difference is: {int(result)}")
    else:
        print(f"The difference is: {result}")

def multiply(a, b):
    result = a * b
    if result.is_integer():
        print(f"The product is: {int(result)}")
    else:
        print(f"The product is: {result}")

def divide(a, b):
    if b == 0:
        print("Undefined!")
    elif a == 0 and b == 0:
        print("Undefined!")
    else:
        result = a / b
        if result.is_integer():
            print(f"The quotient is: {int(result)}")
        else:
            print(f"The quotient is: {result}")
```
- **Purpose:** Performs addition, subtraction, multiplication, and division on two numbers and prints the result.
- **How:**  
  - Each function computes the result and prints it as an integer if the result is whole, or as a float otherwise.
  - The `divide` function checks for division by zero and prints "Undefined!" if division is not possible.

---

### B. **input_checker.py**

##### 1. **Input Validation Functions**
```python
def get_integer(prompt):
    while True:
        value = input(prompt)
        if value.strip().lstrip('-').isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer.")

def get_menu_choice():
    valid_choices = ['1', '2', '3', '4']
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
```
- **Purpose:** Ensures the user enters valid integers for operands and a valid menu choice.
- **How:**  
  - `get_integer` keeps prompting until a valid integer is entered.
  - `get_menu_choice` keeps prompting until the user selects a valid operation.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
from calculator_function import add, subtract, multiply, divide
from input_checker import get_integer, get_menu_choice

def main():
    print("ARITHMETIC CALCULATOR")
    print("----------------------")
    print("[1] - Addition")
    print("[2] - Subtraction")
    print("[3] - Multiplication")
    print("[4] - Division")
    print("----------------------")
    choice = get_menu_choice()

    a = get_integer("Enter first number: ")
    b = get_integer("Enter second number: ")

    if choice == '1':
        add(a, b)
    elif choice == '2':
        subtract(a, b)
    elif choice == '3':
        multiply(a, b)
    elif choice == '4':
        divide(a, b)

if __name__ == "__main__":
    main()
```
- **Purpose:** Provides a menu-driven interface for the user to select an operation and enter two numbers.
- **How:**  
  - Displays the menu and gets a valid choice.
  - Prompts the user for two integers.
  - Calls the appropriate arithmetic function based on the user's choice.