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
FREEZING_FAHRENHEIT = 32

FAHRENHEIT_INPUT = int(input(f"Fahrenheit: "))    
CELSIUS = ((FAHRENHEIT_INPUT - FREEZING_FAHRENHEIT)* 5/9)

if CELSIUS == FREEZING_FAHRENHEIT:
    pass

print ("Temperature (C):", CELSIUS)

