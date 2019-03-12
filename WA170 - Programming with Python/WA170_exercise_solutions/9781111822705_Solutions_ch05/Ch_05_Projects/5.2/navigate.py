"""
File: navigate.py
Project 5.2

Allows the user to navigate to any line in a text file.
"""

# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and read the text
inputFile = open(inName, 'r')
lines = []
for line in inputFile:
    lines.append(line)

# Loop for line numbers from the user until she enters 0
# and prints the line's number followed by the line
while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNumber = int(input("Enter a line number [0 to quit]: "))
    if lineNumber == 0:
        break
    elif lineNumber >= len(lines):
        print("ERROR: line number must be less than", len(lines))
    else:
        print(lineNumber, ": ", lines[lineNumber])
    
