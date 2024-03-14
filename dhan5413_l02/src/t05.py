"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
# Imports

# Constants

Hourly_pay = float(input('Enter the pay per hour: '))
Number_Hours_Worked = float(input('Enter the number of hours worked: '))
TotalPay = Hourly_pay * Number_Hours_Worked
print(f"Total pay for the week: $ {TotalPay:.2f}")