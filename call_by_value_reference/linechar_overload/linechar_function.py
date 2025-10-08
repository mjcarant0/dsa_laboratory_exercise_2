"""
Module to print a line of characters, supporting function overloading.
"""

# Function to print a line of characters
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