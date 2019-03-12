"""
File: shiftright.py
Project 4.5

Shifts the bits in an input string one place to the right.
The rightmost bit wraps around to the leftmost position.
"""

bits = input("Enter a string of bits: ")
if len(bits) > 1:
    bits = bits[-1] + bits[:-1]
print(bits)
