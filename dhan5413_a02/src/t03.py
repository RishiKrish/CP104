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

INPUT = int(input('Enter a date in the format YYYYMMDD: '))

year = (INPUT // 10000)
day = INPUT %100
month = (INPUT //100) % 100

print(f'The reformatted date: {year}/{month}/{day}')
