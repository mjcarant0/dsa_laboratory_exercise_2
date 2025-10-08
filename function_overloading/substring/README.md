<div align="center">

# Substring

</div>

## How the Code Works

### A. **substring_function.py**

##### 1. **Defining the Overloaded Substring Function**
```python
def substring(s, start=None, end=None):
    if start is None and end is None:
        # Print the whole string
        print(f"function substring(str):\n{s}")
    elif end is None:
        # Print substring from start to end
        print(f"function substring(str, {start}):\n{s[start:]}")
    else:
        # Print substring from start to end
        print(f"function substring(str, {start}, {end}):\n{s[start:end+1]}")
```
- **Purpose:** Extracts and displays different parts of a string using simulated function overloading.
- **How:**  
  - With no indices, prints the whole string.
  - With a start index, prints from that index to the end.
  - With both start and end indices, prints from start to end (inclusive).

---

### B. **input_checker.py**

##### 1. **Input Validation for Indices**
```python
def get_valid_index(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        if value.isdigit():
            idx = int(value)
            if min_value <= idx <= max_value: 
                return idx
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a valid integer.")
```
- **Purpose:** Ensures the user enters a valid integer index within the allowed range.
- **How:**  
  - Prompts the user for input.
  - Checks if the input is a digit and within the specified range.
  - Repeats until a valid index is entered.

---

### C. **main.py**

##### 1. **Main Program Logic**
```python
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
```
- **Purpose:** Demonstrates the use of the overloaded substring function.
- **How:**  
  - Displays the original string and its length.
  - Prompts the user for valid start and end indices.
  - Calls the substring function in three ways to show the whole string, from start index, and from start to end index.

---