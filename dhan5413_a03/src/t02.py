"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time

# Constants
print(lawn_mow_time(20.0, 50.0, 4.0))

    if start_num <= 0 or stop_num <= 0:
        print("Both start_num and stop_num should be positive integers.")
        return
    
    print("      ", end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:4}", end="")
    print("\n   "   +"   "+ "----" * (stop_num - start_num + 1))
    
    for i in range(start_num, stop_num + 1):
        print(f"{i:4} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:4}", end="")
        print()
        
