"""
File: testsort.py
Project 6.5

Defines a predicate to test lists for being sorted.

"""

def isSorted(lyst):
    """Returns True if lyst is sorted in ascending
    order or False otherwise."""
    if len(lyst) == 0 or len(lyst) == 1:
        return True
    else:
        for index in range(len(lyst) - 1):
            if lyst[index] > lyst[index + 1]:
                return False
    return True

def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))

main()
