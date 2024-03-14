"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import customer_best
# Constants
print("Find customer with largest balance: ")
filename = "customers.txt"
fh = open(filename, "r+")
result = customer_best(fh)
fh.close()
print (result)