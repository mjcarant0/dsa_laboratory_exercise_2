<div align="center">

# Line Character Overload

</div>

## How the Code Works

### A. **linechar_function.py**

##### 1. **Defining the Overloaded Line Character Function**
```python
def linechar(arg1='*', arg2=None):
    if arg2 is not None:
        # linechar(char, count)
        print(str(arg1) * int(arg2))
    elif isinstance(arg1, int):
        # linechar(count)
        print('*' * arg1)
    else:
        # linechar() or linechar(char)
        print(str(arg1) * 20)
```
- **Purpose:** Prints a line of characters, supporting different ways to call the function (overloading).
- **How:**  
  - If two arguments are provided, prints `arg2` copies of `arg1`.
  - If a single integer is provided, prints that many `*` characters.
  - If called with no arguments or a single character, prints 20 of the specified character (default `*`).

---

### B. **main.py**

##### 1. **Main Program Logic**
```python
from linechar_function import linechar

def main():
    linechar()
    linechar('@')
    linechar(10)
    linechar('#', 15)
    input("Press any key to continue . . .") # Pause the program before exiting

if __name__ == "__main__":
    main()
```
- **Purpose:** Demonstrates the different ways to use the overloaded `linechar` function.
- **How:**  
  - Calls `linechar()` to print 20 `*` characters.
  - Calls `linechar('@')` to print 20 `@` characters.
  - Calls `linechar(10)` to print 10 `*` characters.
  - Calls `linechar('#', 15)` to print 15 `#` characters.
  - Pauses before exiting so the output can be viewed.

---