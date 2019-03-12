"""
File: average.py
Project 6.9
Prints the average of the numbers in a text file 
"""

from functools import reduce

# Accept the input file name and open the file
fileName = input("Enter the input file name: ")
inputFile = open(fileName, 'r')

# Read the numbers as strings into a list
lyst = []
for line in inputFile:
    lyst.extend(line.split())

# Convert all the strings in the list to numbers
lyst = list(map(float, lyst))

# Compute the sum of the numbers
sum = reduce(lambda x, y: x + y, lyst)

# Print the average
if len(lyst) == 0:
    average = 0
else:
    average= sum / len(lyst)
print("The average is", average)
