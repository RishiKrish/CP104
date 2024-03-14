"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-23"
-------------------------------------------------------
"""
# Imports

# Constants
TOTAL_SALES = int(input('Enter the total sales: '))
print('Projected Tax Report')

print('Total sales: $', TOTAL_SALES)
ANNUAL_TAX = float (18.5)

print('Annual Tax : %', ANNUAL_TAX)

TAX = TOTAL_SALES * ANNUAL_TAX/100
print('Tax: $', TAX)
