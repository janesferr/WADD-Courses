"""
File: convert.py
Project 5.6
Defines a function decimalToRep that converts
a number in decimal to a number in a given base. 
"""

# Table of integers in bases 2-16 with digits
repTable = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 :'4',
            5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
            10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',
            14 : 'E', 15 : 'F'}

def decimalToRep(decimal, base):
    """Converts the integer value in decimal to
    a rep in the given base returns the rep as a string."""
    if decimal == 0:
        return '0'
    else:
        rep = ""
        while decimal > 0:
            remainder = decimal % base
            decimal = decimal // base
            rep = repTable[remainder] + rep
        return rep
            

def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

main()
      
