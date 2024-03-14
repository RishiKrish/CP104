"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  RishiKrish DhaneshKumar
ID:      169075413
Email:   dhan5413@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports

# Constants
minued=[]
factors = []
number_list = []
index_list = []
def list_factors(numbers):
    """
    -------------------------------------------------------
    Use: list_factors(numbers) to find the list of numbers that are factors for "i"
    -------------------------------------------------------
    Parameters:
    factors to give all possible outputs
    Returns:
    factors
    ------------------------------------------------------
    """
    for i in range(1, numbers):
        if numbers % i ==0:
            factors.append(i)
    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
        
    while True:
        number = input("Enter a positive number and 0 to stop: ")
        if number == "0":
            break
        number = int(number)
        if number > 0:
            number_list.append(number)
    return number_list
    
            

def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    
    for j in  range(len(numbers)):
        if numbers[j] == target_number:
            index_list.append(j)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    indexes_to_remove = []
    for i in range(len(minuend)):
        if minuend[i] in subtrahend:
            indexes_to_remove.append(i)
    for i in reversed(indexes_to_remove):
        minuend.pop(i)
    return

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """  
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            ans = False, 1 
            break
        else:
            ans = True, -1
            
    return ans
    
    
    