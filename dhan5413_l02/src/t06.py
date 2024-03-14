"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports

# Constants

mortgage_principal_amount = float(input('Enter Mortgage principal: '))

yearpayments = int(input('Enter number of years: '))

interest= float(input('interest rate: '))

monthlyPayment = (interest/12)/100

months = yearpayments*12

monthly = mortgage_principal_amount*(monthlyPayment*(1+monthlyPayment) ** months)/((1+monthlyPayment) ** months-1)

print(monthly)
