"""
Program: equilateral.py
Project 3.1

Determine whether or not three input sides compose an
equilateral triangle.
"""
               
# Request the inputs
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# Determine the result and display it
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
   