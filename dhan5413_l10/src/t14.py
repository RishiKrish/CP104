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
from functions import file_copy_n
# Constants
filename = "words.txt"
filename2 = "new_words.txt"
fh_1 = open(filename, "r+")
fh_2 = open(filename2, "r+")
print("copy 'words.txt' to 'new_words.txt'")
n = int(input("Lines to copy: "))
result = file_copy_n(fh_1, fh_2, n)
fh_1.close()
fh_2.close()