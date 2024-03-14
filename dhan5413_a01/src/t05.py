"""
-------------------------------------------------------
[TASK 5]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""
# Imports

# Constants
Principal = float(input('Enter principal: '))

INTEREST = float(input('Enter the interest: '))
YEARS = int(input('Enter the number of years: '))
N = int(input('How many times is interest compounded in a year'))
A = Principal*(1+((INTEREST/100)/N))**(N*YEARS)
print ('Balance: $', A)