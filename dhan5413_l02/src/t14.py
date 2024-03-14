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

mac_cheese = int(input('Enter the number of mac and cheese: '))

milk = 4/6
butter = 8/6
flour = 0.5/6
salt = 2/6

new_milk = milk * mac_cheese
new_butter = butter * mac_cheese
new_flour = flour * mac_cheese
new_salt = salt * mac_cheese

print(f'{mac_cheese} servings of Mac & Cheese requires:')
print(f'milk (cups): {new_milk}')
print(f'butter (tablespoons): {new_butter}')
print(f'flour (cups): {new_flour}')
print(f'salt (teaspoons): {new_salt}')
