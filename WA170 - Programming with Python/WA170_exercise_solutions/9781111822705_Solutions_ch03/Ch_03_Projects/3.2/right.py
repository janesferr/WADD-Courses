"""
Program: right.py
Project 3.2

Determine whether or not three input sides compose a
right triangle.
"""
               
# Request the inputs
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# Compute the squares
square1 = side1 ** 2
square2 = side2 ** 2
square3 = side3 ** 2

# Determine the result and display it
if square1 + square2 == square3 or \
   square2 + square3 == square1 or \
   square1 + square3 == square2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
   
