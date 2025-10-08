<div align="center">

# Sum of Odd Numbers

</div>

## How the Code Works

### A. **sum_odds.py**

##### 1. **Function to Calculate the Sum of Odd Numbers**
```python
def sum_of_odds(numbers):
    odds = [num for num in numbers if num % 2 != 0] # To filter odd numbers
    return odds, sum(odds)
```
- **Purpose:** Finds all odd numbers in a list and calculates their sum.
- **How:**  
  - Uses a list comprehension to filter out odd numbers from the input list.
  - Returns both the list of odd numbers and their sum.

---

### B. **input_checker.py**

##### 1. **Input Validation for Integers**
```python
def get_int_input(prompt):
    while True:
        value = input(prompt)
        if value.strip().lstrip('-').isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer.")
```
- **Purpose:** Ensures the user enters a valid integer.
- **How:**  
  - Prompts the user for input.
  - Checks if the input is a valid integer (including negatives).
  - Returns the integer if valid, otherwise prompts again.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
from input_checker import get_int_input
from sum_odds import sum_of_odds

def main():
    numbers = []
    for i in range(1, 11):
        num = get_int_input(f"Enter number {i}: ")
        numbers.append(num)
    
    print(f"\nYour numbers: {' '.join(str(n) for n in numbers)}")
    odds, total = sum_of_odds(numbers)
    print(f"Odd numbers: {' '.join(str(n) for n in odds) if odds else 'None'}")
    print(f"The sum of all odd numbers is {total}")

if __name__ == "__main__":
    main()
```
- **Purpose:** Collects 10 integers from the user, displays them, and calculates the sum of all odd numbers.
- **How:**  
  - Uses a loop to collect 10 valid integers.
  - Displays all entered numbers.
  - Calls `sum_of_odds` to get the odd numbers and their sum.
  - Displays the odd numbers and their sum.

---