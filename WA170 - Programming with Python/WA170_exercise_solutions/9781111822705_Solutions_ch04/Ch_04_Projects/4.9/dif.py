"""
File: dif.py
Project 4.9

Deterines whether or not the contents of two text
files are the same.  Outputs "Yes" if that is the
case or "No" and the first two lines that differ if
that is not the case.
"""

# Take the inputs
fileName1 = input("Enter the first file name: ")
fileName2 = input("Enter the second file name: ")

# Open the input files
inputFile1 = open(fileName1, 'r')
inputFile2 = open(fileName2, 'r')

# Read each pair of lines and compare them
while True:
    line1 = inputFile1.readline()
    line2 = inputFile2.readline()
    if line1 == "" and line2 == "":   # Ends of both files
        print("Yes")
        break
    elif line1 != line2:
        print("No")
        print(line1)
        print(line2)
        break
    
