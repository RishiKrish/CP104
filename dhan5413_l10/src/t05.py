"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_append
# Constants
filename = "customers.txt"
fh = open(filename, "r+")
fields = ['35612', 'David', 'Brown', 237.56,'2008-10-10']
result = customer_append(fh, fields)
fh.close()
print("Data: ['35612', 'David', 'Brown', 237.56,'2008-10-10']")
print("data appended to file")
