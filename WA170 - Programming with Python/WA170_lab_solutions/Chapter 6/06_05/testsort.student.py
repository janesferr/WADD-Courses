def isSorted(lyst):
    """Returns True if lyst is sorted in ascending
    order or False otherwise."""

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