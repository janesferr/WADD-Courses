"""
File: reverse.py
Project 11.2

Defines a function to reverse the elements in a list.
The complexity is O(n).
"""

def reverse(lyst):
    """Reverses the elements in a list in linear time."""
    # Use indexes to the first and last element
    # and move them toward each other.
    left = 0
    right = len(lyst) - 1
    while left < right:
        swap(lyst, left, right)
        left += 1
        right -= 1

def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    lyst[x], lyst[y] = lyst[y], lyst[x]

def main():
    """Tests with two lists."""
    lyst = list(range(4))
    reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    reverse(lyst)
    print(lyst)

main()
    
