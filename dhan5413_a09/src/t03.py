"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-29"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics
# Constants
file_handle = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
print(ucount, lcount, dcount, wcount, rcount)
file_handle.close()
