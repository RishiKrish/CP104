"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""
# Imports

# Constants

flyers = int(input('Number of flyers: '))
people = int(input('Number of delivery people: '))

per_person = (flyers // people)
remaining = flyers % people

print(f'Flyers per delivery person: {per_person}')
print(f'Flyers left over: {remaining}')
