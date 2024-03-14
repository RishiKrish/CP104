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
from functions import read_integers
# Constants

file_handle = open("numbers.txt", "r", encoding="utf-8")

read_list = read_integers(file_handle)
print(read_list)
file_handle.close()