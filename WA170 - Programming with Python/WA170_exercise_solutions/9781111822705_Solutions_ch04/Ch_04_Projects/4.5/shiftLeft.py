"""
File: shiftleft.py
Project 4.5

Shifts the bits in an input string one place to the left.
The leftmost bit wraps around to the rightmost position.
"""

bits = input("Enter a string of bits: ")
if len(bits) > 1:
    bits = bits[1:] + bits[0]
print(bits)
