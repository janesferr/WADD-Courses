"""
Program: leibniz.py
Project 3.6

This program approximates the value of pi using an algorithm
designed by the German mathematician Gottfried Leibniz. The
algorithm is as follows:

pi = 4 - 4 / 3 + 4 / 5 - 4 / 7 + . . .

This program allows the user to specify the number of iterations
to use in the approximation.
"""

import math


iterations = int(input("Enter the number of iterations: "))
pioverfour = 0
numerator = 1
denominator = 1
for count in range(iterations):
    pioverfour += numerator / denominator
    numerator = -numerator
    denominator += 2
print("The approximation of pi is", pioverfour * 4)
print("Compare this to the computer's estimation: ", math.pi)
