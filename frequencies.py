"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items: list) -> dict: 
    frequencies = {}
    # Take a list and return a dictionary with key = item in items and value = frequency
    # For each item in items, if the item is in the dictionary, add one to that item with d[str(item)] += 1
    # Otherwise, do frequencies[str(item)] = 0
    for item in items:
        if str(item) in frequencies.keys():
            frequencies[str(item)] += 1
        else:
            frequencies[str(item)] = 1
    return frequencies

if __name__ == "__main__":
    print(frequencies([100,'100',100,"100",'a']))