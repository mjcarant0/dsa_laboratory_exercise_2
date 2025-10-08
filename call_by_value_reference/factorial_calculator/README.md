<div align="center">

# Factorial Calculator

</div>

## How the Code Works

### A. **factorial_function.py**

##### 1. **Defining the Factorial Function (Call by Reference)**
```python
def compute_factorial(n, result_ref):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    result_ref[0] = factorial
```
- **Purpose:** Computes the factorial of a non-negative integer and updates the result by reference.
- **How:**  
  - Initializes `factorial` to 1.
  - Multiplies `factorial` by each integer from 1 to `n`.
  - Stores the result in `result_ref[0]` (a list used to simulate pass by reference).

---

### B. **input_checker.py**

##### 1. **Input Validation Function**
```python
def get_non_negative_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a non-negative integer.")
```
- **Purpose:** Ensures the user enters a valid non-negative integer.
- **How:**  
  - Prompts the user for input.
  - Checks if the input is a non-negative integer using `isdigit()`.
  - If valid, returns the integer.
  - If invalid, prints an error message and repeats.

---

### A. **main.py**

##### 1. **Main Program Logic**
```python
from factorial_function import compute_factorial
from input_checker import get_non_negative_int

def main():
    num = get_non_negative_int("Enter a number: ")
    result = [0]  # Using a list to simulate pass by reference
    compute_factorial(num, result)
    print(f"The factorial of {num} is {result[0]}")

if __name__ == "__main__":
    main()
```
- **Purpose:** Handles user interaction and displays the factorial result.
- **How:**  
  - Imports the necessary functions.
  - Gets a valid non-negative integer from the user.
  - Calls `compute_factorial` to compute the factorial and store it by reference.
  - Prints the result in the required format.