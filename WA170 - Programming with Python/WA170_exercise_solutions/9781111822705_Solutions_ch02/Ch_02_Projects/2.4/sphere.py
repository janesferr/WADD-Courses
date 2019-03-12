"""
Program: sphere.py
Project 2.4

Given the radius compute the diameter, circumference, and volume
of a sphere.

Useful facts:
   diameter = 2 * radius
   circumference = diameter * 3.14
   surface area = 4 * PI * radius * radius
   volume = 4/3 * PI * radius * radius * radius

"""

import math
               
# Request the input
radius = float(input("Enter the sphere's radius: "))  

# Compute the results
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4/3.0 * math.pi * radius * radius * radius

# Display the results
print("Diameter     :", diameter)
print("Circumference:", circumference)
print("Surface area :", surfaceArea)
print("Volume       :", volume)
