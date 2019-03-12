"""
File: decimaltooctal.py
Project 4.4

Converts a decimal integer to a string of octal digits.
"""

decimal = int(input("Enter a decimal integer: "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder Octal")
    ostring = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        ostring = str(remainder) + ostring
        print("%5d%8d%12s" % (decimal, remainder, ostring))
    print("The octal representation is", ostring)  
