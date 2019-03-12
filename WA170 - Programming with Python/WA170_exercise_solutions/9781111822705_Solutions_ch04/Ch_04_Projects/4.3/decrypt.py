"""
File: decrypt.py
Project 4.3

Decypts a file of encrypted text. and prints
the result.  The other input is the distance value.
"""

# The ASCII values range from 0 through 127

# Take the inputs
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

# Open the input file and read the encrypted text
inputFile = open(inName, 'r')
code = inputFile.read()


# Open the output file and write the decrypted text
outFile = open(outName, 'w')
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - \
                      (distance - (1 - ordValue))
    plainText +=  chr(cipherValue)
outFile.write(plainText)
outFile.close()
