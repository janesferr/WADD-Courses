"""
Program: gcd.py
Project 3.8

Compute and print the greatest common divisor of two input
integers.
"""

first = int(input("Enter the smaller number: "))
second = int(input("Enter the larger number: "))

while first > 0:
    remainder = second % first
    second = first
    first = remainder

print("The greatest common divisor is", second)
