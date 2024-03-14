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
from functions import line_numbering

# Constants

with open("wilde.txt", "r", encoding="utf-8") as fh_read:
    with open("wilde_numbered.txt", "w", encoding="utf-8") as fh_write:
        line_numbering(fh_read,fh_write)
        print("line numbering is completed check the wilde_numbered.txt file")