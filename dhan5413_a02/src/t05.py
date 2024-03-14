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

length = float(input('foundation length: '))
width = float(input('foundation width: '))
height = float(input('foundation height: '))
wall = float(input('foundation wall height: '))

COST_CONCRETE = float(input('enter cost of concrete: '))
COST_BRICKS = float(input('enter cost of bricks: '))

concrete = float(length * width * height)
total_cost_concrete = float(COST_CONCRETE * concrete)

bricks = float(2 * (length * wall + wall * width))
total_cost_bricks = float(bricks * COST_BRICKS)

TOTAL_COST = float(total_cost_concrete + total_cost_bricks)

print(f'Concrete needed for foundation (m^3): {concrete:.2f}')
print(f'Cost of concrete: ${total_cost_concrete:.2f}')
print(f'Bricks needed for walls (m^2): {bricks:.2f}')
print(f'Cost of bricks: ${total_cost_bricks:.2f}')
print(f'Total cost : ${TOTAL_COST:.2f}')


