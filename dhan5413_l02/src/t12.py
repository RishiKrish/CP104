"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
# Imports

# Constants

SECONDS = int(input('Enter the number of seconds:'))

DAYS = SECONDS // (24*60*60)
LEFT_SEC = SECONDS % (24*60*60)
HOURS = LEFT_SEC // (60*60)
LEFT_SEC = LEFT_SEC % (60*60)
MINUTES = LEFT_SEC // 60
LEFT_SEC = LEFT_SEC % 60

print(f"Days: {DAYS} Hours: {HOURS} Minutes: {MINUTES} Seconds: {LEFT_SEC}")