"""
File: concordance.py
Project 5.8

Prints the unique words in a text file and their frequences.
"""

# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and initialize list of unique words
inputFile = open(inName, 'r')
uniqueWords = {}

# Add the unique words in the file to the list
for line in inputFile:
    words = line.split()
    for word in words:
        freq = uniqueWords.get(word, None)
        if freq == None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = freq + 1

# Prints the unique words and their frequencies,
# in alphabetical order
words = list(uniqueWords.keys())
words.sort()
for word in words:
    print(word, uniqueWords[word])
