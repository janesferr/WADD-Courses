"""
File: decrypt.py
Project 4.7

Decypts an input string of characters and prints
the result.
"""

code = input("Enter the coded text: ")
wordList = code.split()
plainText = ""
for word in wordList:
    # Shift one bit to right
    word = word[-1] + word[:-1]
    # Convert to decimal
    decimal = 0
    exponent = len(word) - 1
    for digit in word:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
    # Subtract 1 from ASCII value
    decimal -= 1
    # Convert to a character and add to code string
    plainText += chr(decimal)
print(plainText)
