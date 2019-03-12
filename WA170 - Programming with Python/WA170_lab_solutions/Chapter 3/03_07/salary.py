"""
Program: salary.py
Project 3.7

Compute a school district's salary schedule.

Inputs 
   starting salary
   annual percentage increase
   number of years for which to print the schedule

Outputs
    Two columns containing the year and the salary
    after the increase.
"""

# Accept the inputs
startSal = float(input("Enter the starting salary: $"))
increase = int(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

# Compute and display the results
print("Year   Salary\n-------------")
multiplier = 1 + increase / 100
nextSal = startSal
for year in range(1, years + 1):
    print("%2d%12.2f" % (year, nextSal))
    nextSal *= multiplier 