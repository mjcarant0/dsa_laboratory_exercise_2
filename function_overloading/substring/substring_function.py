"""
Module for substring functions with simulated overloading.
"""

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