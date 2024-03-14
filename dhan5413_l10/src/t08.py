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
from functions import append_increment
# Constants
filename = "numbers.txt"
fh = open(filename, "r+")
result = append_increment(fh)
fh.close()
print("file 'numbers.txt' open for reading and writing")
print("14 is appended")
