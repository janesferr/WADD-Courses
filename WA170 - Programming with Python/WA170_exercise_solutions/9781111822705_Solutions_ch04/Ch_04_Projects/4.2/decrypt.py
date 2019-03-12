"""
File: decrypt.py
Project 4.2

Decypts an input string characters and prints
the result.  The other input is the distance value.
"""

# The ASCII values range from 0 through 127

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - \
                      (distance - (1 - ordValue))
    plainText +=  chr(cipherValue)
print(plainText)
