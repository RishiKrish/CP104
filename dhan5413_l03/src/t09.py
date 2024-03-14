"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""
# Imports

# Constants

SWEATBAND = float(input('Enter the cost(Sweatband): $'))
PANT = float(input('Enter the cost(Pant): $'))
JACKET = float(input('Enter the cost(Jacket): $'))

TOTAL = SWEATBAND+PANT+JACKET

print("Clothes      Cost")
print(f"Sweatband   ${SWEATBAND:6.2f}")
print(f"Pant        ${PANT:6.2f}")
print(f"Jacket      ${JACKET:6.2f}")
print(f"Total       ${TOTAL:6.2f}")