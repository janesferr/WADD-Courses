"""
Program: population.py
Project 3.5

Predict popultation growth, assuming that no
organisms die.

Inputs:
   initial number of organisms
   rate of growth (a float > 1)
   the number of hours to achieve the rate
   number of hours of growth
"""

# Accept the inputs

number = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth [a real number > 1]: "))
cycleHours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalHours = int(input("Enter the total hours of growth: "))

# Calculate the number of cycles

cycles = totalHours // cycleHours

# Calculate the population after an integral number of cycles

for eachPass in range(cycles):
    number = number * rate

print("The total population is", int(number))
