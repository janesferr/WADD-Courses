"""
File: tidbit.py
Project 9.6

Data model to produce a payment schedule for a loan to purchase a computer.

Initial data from user:
   purchase price, annual interest rate

Other data facts:
   downpayment = 10% of purchase price
   monthly payment = 5% of purchase price

Example usage:

print Tidbit(2500.00, 5)
   
"""

class Tidbit(object):

    def __init__(self, purchasePrice, rate):
        """Sets up the data for the model."""
        self._purchasePrice = purchasePrice
        self._monthlyRate = rate / 100.0 / 12.0
        self._downPayment = purchasePrice * 0.1
        
    def __str__(self):
        """Returns a formatted loan schedule."""
        schedule =  "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n"
        balance = self._purchasePrice - self._downPayment
        monthlyPayment = 0.05 * balance
        month = 1
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * self._monthlyRate
            principal = monthlyPayment - interest
            remaining = balance - monthlyPayment
            schedule += "%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % (month, balance, interest, principal, monthlyPayment, remaining)
            balance = remaining
            month += 1
        return schedule
