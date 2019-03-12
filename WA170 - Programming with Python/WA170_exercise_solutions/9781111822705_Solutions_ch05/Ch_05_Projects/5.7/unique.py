"""
File: unique.py
Project 5.7

Prints the unique words in a text file in alphabetical order.
"""

# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and initialize list of unique words
inputFile = open(inName, 'r')
uniqueWords = []

# Add the unique words in the file to the list
for line in inputFile:
    words = line.split()
    for word in words:
        if not word in uniqueWords:
            uniqueWords.append(word)
uniqueWords.sort()

# Prints the unique words
for word in uniqueWords:
    print(word)
    
