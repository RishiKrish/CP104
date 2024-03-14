"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants

DIAMETER = float (input(f'Enter the diameter of base (cm): '))
HEIGHT = float (input (f'Enter the height of container (cm): '))
COST = float (input(f'Enter the cost of material ($/cm^2) : '))
NUMBER_OF_CONTAINERS = int(input('Enter the number of containers: '))

PiRADIUS = (3.14)

RADIUS = (DIAMETER / 2 )

SA = 2 * (PiRADIUS * RADIUS ** 2) + HEIGHT * (2 * PiRADIUS * RADIUS)
COUNT_AREA = SA - (PiRADIUS * RADIUS ** 2) 

ONE = ( COUNT_AREA* COST)

TOTAL = ONE*NUMBER_OF_CONTAINERS 

print('THIS IS COST OF ONE CONTAINER: $', ONE)

print('THIS IS THE COST OF ALL CONTAINERS: $ ', TOTAL)
