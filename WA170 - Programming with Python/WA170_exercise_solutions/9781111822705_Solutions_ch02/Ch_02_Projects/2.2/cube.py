"""
Program: cube.py
Project 2.2

Compute the surface area of a cube.

The input is the cube's edge. 
The output is the surface area of the cube.
"""
               
# Request the input
edge = float(input("Enter the cube's edge: "))  

# Compute the surface area
surfaceArea = edge * edge * 6

# Display the surface area
print("The surface area is", surfaceArea, "square units.")
