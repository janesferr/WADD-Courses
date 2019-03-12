"""
Program: klickstonauts.py
Project 2.9

Convert kilometers to nautical miles.

Useful facts:
   1 kilometer = 1/10000 of the distance between the North Pole and the Equator
   there are 90 degrees between the North Pole and the Equator
   1 degree = 60 minutes of arc
   1 nautical mile =  1 minute of arc


"""         

# Request the input
klicks = float(input("Enter the number of kilometers: "))  

# Compute the result
nauts = klicks * 90 * 60 / 10000.0

# Display the result
print("The number of nautical miles is", nauts)
