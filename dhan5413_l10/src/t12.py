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
from functions import find_shortest
# Constants
filename = "words.txr"
fh = open(filename, "r+")
result = find_shortest(fh)
fh.close()
print("file 'words.txt open for reading")
print(f"'{result}' is the last shortest word")