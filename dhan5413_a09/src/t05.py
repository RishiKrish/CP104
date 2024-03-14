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
from functions import student_stats
# Constants


with open("students.txt", "r", encoding="utf-8") as file_handle:
    l_id, h_id, avg = student_stats(file_handle)
    print(f"Lowest ID:{l_id}, Highest id:{h_id}, Average Mark: {avg:.2f}")