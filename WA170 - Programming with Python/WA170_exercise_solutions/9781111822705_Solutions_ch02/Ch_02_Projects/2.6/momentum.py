"""
Program: momentum.py
Project 2.6

Given an object's mass and velocity, compute its momentum
and kinetic energy.

"""
               
# Request the input
mass = float(input("Enter the object's mass: ")) 
velocity = float(input("Enter the object's velocity: "))  

# Compute the results
momentum = mass * velocity
kineticEnergy = (mass * velocity ** 2) / 2

# Display the results
print("The object's momentum is", momentum)
print("The object's kinetic energy is", kineticEnergy)
