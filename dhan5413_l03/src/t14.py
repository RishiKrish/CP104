"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports

# Constants

total_minutes = int(input('Enter the number of minutes: '))

minutes = total_minutes // 60
remaining_minutes = total_minutes % 60

days = minutes // 24
hours = minutes % 24


#print ('There are',days,'days',hours,'hours and',remaining_minutes,'minutes in', total_minutes,'minutes')

print(f'There are {days} days, {hours} hours, and {remaining_minutes} minutes in {total_minutes} minutes')  