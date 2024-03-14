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

NUMBER = int(input('Enter the number: '))

if 10 <= NUMBER <=99:
    TENTH = NUMBER // 10
    ONES = NUMBER % 10
    
    difference = int(TENTH - ONES)
    
print(f'The difference of the digits of 25 is {difference}')