"""
File: octaltodecimal.py
Project 4.4

Converts a string of octal digits to a decimal integer.
"""

ostring = input("Enter a string of octal digits: ")
decimal = 0
exponent = len(ostring) - 1
for digit in ostring:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
