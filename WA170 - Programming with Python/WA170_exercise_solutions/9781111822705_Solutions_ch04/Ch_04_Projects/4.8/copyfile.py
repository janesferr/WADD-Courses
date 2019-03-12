"""
File: copyfile.py
Project 4.8

Copies the text from a given input file to a given
output file.
"""

# Take the inputs
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")

# Open the input file and read the text
inputFile = open(inName, 'r')
text = inputFile.read()

# Open the output file and write the text
outFile = open(outName, 'w')
outFile.write(text)
outFile.close()
