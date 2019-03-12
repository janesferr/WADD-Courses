"""
File: decrypt.py
Decypts an input string of lowercase letters and prints
the result.  The other input is the distance value.
"""

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordValue + 1))
    plainText +=  chr(cipherValue)
print(plainText)
