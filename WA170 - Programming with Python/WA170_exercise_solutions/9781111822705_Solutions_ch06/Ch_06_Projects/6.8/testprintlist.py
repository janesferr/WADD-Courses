"""
File: testprintlist.py
Project 6.8

Defines the printAll function with a trace.

Before each recursive call, the function creates
a slice of its nonempty list argument.  The hidden cost
is that each slice produces a copy of the list, less
its first item.  This process requires time and memory.

"""
    

def printAll(seq):
    if seq:
        print(seq, "->", seq[0])
        printAll(seq[1:])

printAll(list(range(10)))

