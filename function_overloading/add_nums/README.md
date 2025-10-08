<div align="center">

# Add Numbers

</div>

## How the Code Works

### A. **add_function.py**

##### 1. **Defining Overloaded Add Functions**
```python
def add(a, b, c=None, d=None):
    if c is None and d is None:
        # Two arguments
        return a + b
    elif d is None:
        # Three arguments
        return a + b + c
    else:
        # Four arguments
        return sum([a, b, c, d])

def add_array(arr):
    return sum(arr)
```
- **Purpose:** Provides overloaded functions to add two, three, or four numbers, and a function to add all elements in an array.
- **How:**  
  - The `add` function uses default arguments to handle two, three, or four numbers.
  - The `add_array` function sums all elements in a list (array).

---

### B. **input_checker.py**

##### 1. **Input Validation for Multiple Integers**
```python
def get_ints(prompt, count):
    while True:
        try:
            values = input(prompt).split()
            if len(values) != count:
                print(f"Please enter exactly {count} numbers.")
                continue
            nums = [int(v) for v in values]
            return nums
        except ValueError:
            print("Invalid input. Please enter integers only.")
```
- **Purpose:** Ensures the user enters the correct number of valid integers, separated by spaces.
- **How:**  
  - Prompts the user for input and splits the input by spaces.
  - Checks if the correct number of values is entered.
  - Converts each value to an integer, or prompts again if invalid.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
from add_function import add, add_array
from input_checker import get_ints

def main():
    nums2 = get_ints("Enter two numbers (separate with space): ", 2)
    print(f"The sum is: {add(nums2[0], nums2[1])}")

    nums3 = get_ints("Enter three numbers (separate with space): ", 3)
    print(f"The sum is: {add(nums3[0], nums3[1], nums3[2])}")

    nums4 = get_ints("Enter four numbers (separate with space): ", 4)
    print(f"The sum is: {add_array(nums4)}")

if __name__ == "__main__":
    main()
```
- **Purpose:** Demonstrates function overloading by adding two, three, or four numbers as requested.
- **How:**  
  - Prompts the user for two, three, and four numbers (with clear instructions).
  - Uses the appropriate add function for each case.
  - Prints the sum for each set of numbers.

---