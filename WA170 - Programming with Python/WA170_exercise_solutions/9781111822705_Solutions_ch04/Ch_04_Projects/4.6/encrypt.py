"""
File: encrypt.py
Probject 4.6

Encypts an input string of characters and prints
the result.
"""

plainText = input("Enter a message: ")

code = ""
for ch in plainText:
    # Add 1 to ASCII value
    ordValue = ord(ch) + 1
    # Convert to binary
    bstring = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bstring = str(remainder) + bstring
    # Shift one bit to left
    if len(bstring) > 1:
        bstring = bstring[1:] + bstring[0]
    # Add encrypted character to code string
    code += bstring + " "
print(code)
